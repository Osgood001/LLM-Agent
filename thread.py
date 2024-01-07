import json
import os
import time

import openai
from openai import OpenAI

import functions
from tools.mathematica import query_wolframalpha

# Check OpenAI version compatibility
from packaging import version
from dotenv import load_dotenv
load_dotenv()

required_version = version.parse("1.1.1")
current_version = version.parse(openai.__version__)
# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_API_KEY = "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"
if current_version < required_version:
  raise ValueError(
      f"Error: OpenAI version {openai.__version__} is less than the required version 1.1.1"
  )
else:
  print("OpenAI version is compatible.")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# # Create or load assistant
# assistant_id = functions.create_assistant(
#     client)  # this function comes from "functions.py"

def create_thread(client):
    # Function to create a new thread and return its ID
    try:
        response = client.beta.threads.create()  # No assistant_id needed
        thread_id = response.id
        return thread_id
    except Exception as e:
        print(f"Error creating thread: {e}")
        return None

def chat(user_input, assistant_id, thread_id=None):
    if thread_id is None:
        thread_id = create_thread(client)
        if thread_id is None:
            return json.dumps({"error": "Failed to create a new thread"})

    print(f"Received message: {user_input} in thread {thread_id}")

    # Run the Assistant
    try:
        # Add the user's message to the thread
        client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=user_input
        )

        # Start the Assistant Run
        run = client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id
        )

        # Check if the Run requires action (function call)
        while True:
            run_status = client.beta.threads.runs.retrieve(
                thread_id=thread_id,
                run_id=run.id
            )

            if run_status.status == 'completed':
                break
            elif run_status.status == 'requires_action':
                tool_outputs = []
                for tool_call in run_status.required_action.submit_tool_outputs.tool_calls:
                    # Extract the arguments from the tool call
                    tool_name = tool_call.function.name
                    tool_arguments = tool_call.function.arguments
                    tool_call_id = tool_call.id
                    # Execute the tool
                    if tool_name == 'query_wolframalpha':
                        # Query wolframalpha
                        result = str(query_wolframalpha(tool_arguments))
                        # Prepare the tool output
                        tool_output = {
                            "tool_call_id": tool_call_id,
                            "output": result
                        }
                        tool_outputs.append(tool_output)
                # Submit the tool outputs
                run = client.beta.threads.runs.submit_tool_outputs(
                    thread_id=thread_id,
                    run_id=run.id,
                    tool_outputs=tool_outputs
                )
                time.sleep(1)  # Wait for a second before checking again

        # Retrieve and return the latest message from the assistant
        messages = client.beta.threads.messages.list(thread_id=thread_id)
        assistant_message = messages.data[0].content[0].text.value

        formatted_message = assistant_message # keep it unchanged

        # response_data = json.dumps({"response": assistant_message, "thread_id": thread_id})
        return formatted_message

    except Exception as e:
        print(f"An error occurred: {e}")
        error_response = json.dumps({"error": str(e)})
        return error_response

def load_assistant(index, presets):
    if index == len(presets) + 1:
        name = input("Please enter the new assistant's name (optional, press enter to skip): ")
        description = input("Please enter the new assistant's description (optional, press enter to skip): ")
        file_path = input("Please enter the new assistant's file path (optional, press enter to skip): ")
        tools = input("Please enter the tools used by the new assistant (optional, press enter to skip): ")
        prompt = input("Please enter the new assistant's prompt (optional, press enter to skip): ")
        assistant_id = functions.create_assistant(client, name, description, file_path, tools, prompt)
    else:
        preset = presets[str(index)]
        assistant_id = functions.create_assistant(client, preset['name'], preset['description'], preset['file_path'], preset['tools'], preset['prompt'])
    return assistant_id

if __name__ == '__main__':
    print("Hello \n Welcome to the Agent System. \n We provide you with the following chatbots:")
    presets_file_path = 'preset.json'
    if os.path.exists(presets_file_path):
        with open(presets_file_path, 'r') as file:
            presets = json.load(file)
            for i, key in enumerate(presets.keys()):
                print(f"{i+1}. {presets[key]['name']}: {presets[key]['description']}")
            print(f"{len(presets)+1}. Create a new assistant")
        selected_index = int(input("\n Please enter the index of your choice: "))
    else:
        print("No presets found. Creating a new assistant.")
        selected_index = 1
        presets = {}

    if selected_index == len(presets) + 1:
        name = input("Enter the name of the new assistant: ")
        description = input("Enter a description for the new assistant: ")
        file_path = input("Enter the file path for the new assistant: ")
        tools = input("Enter the tools used by the new assistant: ")
        prompt = input("Enter the prompt for the new assistant: ")
        assistant_id = functions.create_assistant(client, name, description, file_path, tools, prompt)
    else:
        assistant_id = load_assistant(selected_index, presets)

    thread_id = create_thread(client)
    while True:
        user_input = input("Enter your message: ")
        if user_input == "exit":
            print("Goodbye!")
            break
        response = chat(user_input, assistant_id, thread_id)
        print(response)