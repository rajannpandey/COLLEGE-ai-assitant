from llm.router import choose_tool
from tools.executor import execute_tool
def process_request(user_input):
    # Step 1: Ask Hugging Face which tool to use
    tool_request = choose_tool(user_input)
    # Step 2: Execute the selected Python tool
    tool_result = execute_tool(tool_request)
    # Step 3: Return both the tool and result
    return {
        "user_request": user_input,
        "tool_used": tool_result["tool_used"],
        "result": tool_result["result"]
    }
