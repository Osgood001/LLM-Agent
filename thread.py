import json
import os
import time

import openai
from openai import OpenAI

import functions

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

# Create or load assistant
assistant_id = functions.create_assistant(
    client)  # this function comes from "functions.py"

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
                # Here you can handle specific actions if your assistant requires them
                # ...
                time.sleep(1)  # Wait for a second before checking again

        # Retrieve and return the latest message from the assistant
        messages = client.beta.threads.messages.list(thread_id=thread_id)
        assistant_message = messages.data[0].content[0].text.value

        # 将换行符替换为一个空格
        # formatted_message = assistant_message.replace("\n", " ")
        formatted_message = assistant_message # keep it unchanged

        # response_data = json.dumps({"response": assistant_message, "thread_id": thread_id})
        return formatted_message

    except Exception as e:
        print(f"An error occurred: {e}")
        error_response = json.dumps({"error": str(e)})
        return error_response


if __name__ == '__main__':
    # file_path =  input("Input the path of the file you want to upload: ")
    assistant_id = functions.create_assistant(client)
    thread_id = create_thread(client)
    while True:
        user_input = input("Enter your message: ")
        if user_input == "exit":
            print("哈哈，拜拜了您嘞！")
            break
        response = chat(user_input, assistant_id, thread_id)
        print(response)
   
    