import json
import subprocess

wolframscript = "C:/Program Files/Wolfram Research/Mathematica/13.2/wolfram.exe"

def query_wolframalpha(query):
    query = json.loads(query)['query']
    print("\n Querying Wolfram Alpha for information...")
    print(f"Query: {query}")
    # Command to execute via wolframscript
    command = ['wolframscript', '-code', f'WolframAlpha["{query}"]']
    # command = ['wolframscript', '-code', f'{query}']

    # Run wolframscript to get information
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Get output and error messages
    output, error = process.communicate()

    # Decode the output and error messages
    output = output.decode('utf-8', errors='ignore') if output else None
    error = error.decode('utf-8', errors='ignore') if error else None

    # Create a dictionary to store the output and error
    result = {
        'output': output,
        'error': error
    }
    
    print("Query complete.")
    print(f"\nOutput: {output}\n")

    return result

tool_wolframalpha = {
    "type": "function",
    "function": {
        "name": "query_wolframalpha",
        # "description": "Query Wolfram Alpha for information, use mathematica format query would make it better",
        "description": "Write mathematica code for information or computation, fix the code if output errror",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Mathematica code,when calling wolframe alpha, you should write mathematica code isntead of natural language"
                }
            },
            "required": ["query"]
        }
    }
}

# Test the function
if __name__ == '__main__':
    path = r"C:\D\Cloud\OneDrive\应用\remotely-save\Obsidian_Osgood\3.Practice\LLM Agent\test.json"
    with open(path, 'r') as f:
        result = query_wolframalpha(f.read())
    print(result)