from thread import *

if __name__ == '__main__':
    print("Hello \n Welcome to the Agent System. \n We provide you with the following chatbots:")
    presets_file_path = 'config/preset.json'
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