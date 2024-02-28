import json
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
from tools.mathematica import tool_wolframalpha

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Init OpenAI Client
client = OpenAI(api_key=OPENAI_API_KEY)

def create_assistant(client, name, description, file_path, tools, prompt):
  assistant_file_path = 'preset.json'

  # Load existing data
  if os.path.exists(assistant_file_path):
    with open(assistant_file_path, 'r') as file:
      data = json.load(file)
  else:
    data = {}

  # Check if assistant already exists
  for key, assistant_data in data.items():
    if assistant_data['name'] == name:
      print(f"Loaded existing assistant ID for {name}.")
      return assistant_data['assistant_id']

  # If no assistant.json is present, create a new assistant using the below specifications
  if not os.path.exists(file_path):
    file = client.files.retrieve("file-Wp3snAIbfaGk3Riy6TAwiffZ")
  else:
    file = client.files.create(file=open(file_path, "rb"), purpose='assistants')

  assistant = client.beta.assistants.create(
    name=name,
    description=description,
    instructions=prompt,
    model="gpt-3.5-turbo-1106",
    tools=[
      {
        'type': tools,
      },
      tool_wolframalpha, 
      ],
    file_ids=[file.id])

  # Add new assistant data
  data[str(len(data) + 1)] = {
    'name': name,
    'assistant_id': assistant.id,
    'tools': tools,
    'file_path': file_path,
    'description': description,
    'prompt': prompt
  }

  # Save updated data
  with open(assistant_file_path, 'w') as file:
    json.dump(data, file)

  print(f"Created a new assistant named {name} and saved the ID.")
  return assistant.id
