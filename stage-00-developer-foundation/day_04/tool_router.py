# Define individual tool functions
def calculator(expression):
    try:
        # Simple string math evaluator for basic mathematical operations
        result = eval(expression)
        return f"Calculation Result: {result}"
    except Exception:
        return "Error: Invalid mathematical expression."

def weather(city):
    # Simulated weather lookup tool
    return f"Weather Report: Clear skies and 24°C in {city}."

def search(query):
    # Simulated search tool
    return f"Search Results: Top links and context found for '{query}'."

# Tool Registry (Dictionary mapping names to function objects)
tools = {
    "calculator": calculator,
    "weather": weather,
    "search": search
}

def run_tool_router():
    print("===== AGENTIC TOOL ROUTER =====")
    print("Available tools:", ", ".join(tools.keys()))
    
    # 1. Capture tool choice
    selected_tool_name = input("\nWhich tool do you want to use? ").strip().lower()

    # 2. Look up the function in the tools dictionary
    if selected_tool_name in tools:
        tool_function = tools[selected_tool_name]

        # 3. Get relevant input based on chosen tool
        if selected_tool_name == "calculator":
            arg = input("Enter math expression (e.g., 10 + 5 * 2): ")
        elif selected_tool_name == "weather":
            arg = input("Enter city name: ")
        elif selected_tool_name == "search":
            arg = input("Enter search query: ")

        # 4. Execute the mapped function
        result = tool_function(arg)
        print("\n[Tool Output]:", result)
    else:
        print(f"Error: Tool '{selected_tool_name}' is not recognized.")

if __name__ == "__main__":
    run_tool_router()