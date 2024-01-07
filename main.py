# This file aims at building the basic workflow of calling an agent from our preset.
# client = OpenAI(api_key="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") # supply your API key however you choose
import argparse
import importlib
import json

from openai import OpenAI
API_KEY=  "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"

def create_assistant(tool_name):
    # 获取OpenAI的客户端
    client = OpenAI(api_key=API_KEY)

    # 创建一个新的助手
    assistant = client.beta.assistants.create(
        instructions="You are a personal math tutor. When asked a math question, write and run code to answer the question.",
        model="gpt-3.5-turbo",
        tools=[{"type": tool_name}],
    )

    # 返回新的助手ID和工具列表
    return assistant.id, [tool_name]

def call_openai_agent(file_id, assistant_id):
    """
    Call the OpenAI agent with the given file ID and assistant ID.

    Args:
        file_id (str): The ID of the file to retrieve.
        assistant_id (str): The ID of the assistant to retrieve.

    Returns:
        tuple: A tuple containing the retrieved assistant and file.
    """
    client = OpenAI(api_key=API_KEY)
    file = client.files.retrieve(file_id)
    assistant = client.beta.assistants.retrieve(assistant_id)
    return assistant, file

def call_tool(tool_name, prompt):
    """
    Calls a tool module based on the given tool name and runs it with the provided prompt.

    Args:
        tool_name (str): The name of the tool module to be called.
        prompt (str): The prompt to be passed to the tool module.

    Returns:
        None
    """
    tool_module = importlib.import_module(f'tools.{tool_name}')
    tool_module.run(prompt)

def get_assistant_id(tool_name):
    # 从文件中加载助手ID和工具列表
    with open('assistants.json', 'r') as f:
        assistant_ids = json.load(f)

    # 检查是否存在符合要求的助手ID
    for id, tools in assistant_ids.items():
        if tool_name in tools and check_requirements(id):
            return id, tools

    # 如果没有找到符合要求的助手ID，创建一个新的助手ID
    id, tools = create_assistant(tool_name)
    assistant_ids[id] = tools

    # 将新的助手ID和工具列表保存到文件中
    with open('assistants.json', 'w') as f:
        json.dump(assistant_ids, f)

    return id, tools

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Call OpenAI agent and tools.')
    parser.add_argument('--file_path', type=str, required=True, help='File path to be processed.')
    parser.add_argument('--tool', type=str, required=True, help='Tool to be used.')
    parser.add_argument('--prompt', type=str, required=True, help='Prompt for the tool.')
    args = parser.parse_args()

    assistant_id, tools = get_assistant_id(args.tool)

    assistant, file = call_openai_agent(file_id, assistant_id)
    call_tool(args.tool, args.prompt)