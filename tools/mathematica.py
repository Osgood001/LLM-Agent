import json
import subprocess

wolframscript = "C:/Program Files/Wolfram Research/Mathematica/13.2/wolframscript.exe"

def query_wolframalpha(query):
    query = json.loads(query)['query']
    print("\n Querying Wolfram Alpha for information...")
    print(f"Query: {query}")
    # Command to execute via wolframscript
    command = ['wolframscript', '-code', f'WolframAlpha["{query}"]']

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
        "description": "Query Wolfram Alpha for information",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The query to send to Wolfram Alpha"
                }
            },
            "required": ["query"]
        }
    }
}

# Test the function
if __name__ == '__main__':
    result = query_wolframalpha('current weather in Beijing')
    print(result)