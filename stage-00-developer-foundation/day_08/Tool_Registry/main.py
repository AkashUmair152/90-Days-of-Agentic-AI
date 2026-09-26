from typing import Any, Protocol


class Tool:
    """Base class for all tools in the registry."""

    def __init__(self, name: str, description: str) -> None:
        self.name: str = name
        self.description: str = description

    def run(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError("Subclasses must implement the run() method.")


# --- Tool Implementations ---


class CalculatorTool(Tool):

    def __init__(self) -> None:
        super().__init__(
            name="calculator",
            description="Performs simple arithmetic operations.",
        )

    def run(self, a: int | float, b: int | float, op: str = "+") -> int | float:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b if b != 0 else "Error: Division by zero"
        else:
            raise ValueError(f"Unsupported operator: {op}")


class TextTool(Tool):

    def __init__(self) -> None:
        super().__init__(
            name="text", description="Converts text strings to uppercase."
        )

    def run(self, text: str) -> str:
        return text.upper()


class GreetingTool(Tool):

    def __init__(self) -> None:
        super().__init__(
            name="greeting",
            description="Generates a personalized greeting message.",
        )

    def run(self, name: str) -> str:
        return f"Hello, {name}! Welcome to the Tool Registry."


# --- Registry Management Functions ---


def register_tool(registry: list[Tool], tool: Tool) -> None:
    """Adds a tool to the registry if it isn't already present."""
    if not any(t.name == tool.name for t in registry):
        registry.append(tool)
        print(f"✅ Registered tool: '{tool.name}'")
    else:
        print(f"⚠️ Tool '{tool.name}' is already registered.")


def remove_tool(registry: list[Tool], name: str) -> bool:
    """Removes a tool from the registry by name."""
    initial_length = len(registry)
    registry[:] = [tool for tool in registry if tool.name != name]

    if len(registry) < initial_length:
        print(f"🗑️ Removed tool: '{name}'")
        return True

    print(f"❌ Tool '{name}' not found in registry.")
    return False


def find_tool(registry: list[Tool], name: str) -> Tool | None:
    """Searches through the tools and returns the matching Tool instance."""
    matching_tools = [tool for tool in registry if tool.name == name]
    return matching_tools[0] if matching_tools else None


def list_tools(registry: list[Tool]) -> list[dict[str, str]]:
    """Returns a formatted list of dictionary summaries for all registered tools using list comprehension."""
    return [
        {"name": tool.name, "description": tool.description} for tool in registry
    ]


# --- Driver / Execution ---

if __name__ == "__main__":
    # Initialize Registry with initial tools using list comprehension / direct list
    tools: list[Tool] = [CalculatorTool(), TextTool()]

    # Bonus: Register a new tool dynamically
    register_tool(tools, GreetingTool())

    print("\n--- Current Registered Tools ---")
    tool_summaries = list_tools(tools)
    for info in tool_summaries:
        print(f"• {info['name']}: {info['description']}")

    print("\n--- Running Tool Tests ---")

    # Test CalculatorTool
    calc = find_tool(tools, "calculator")
    if calc:
        result = calc.run(20, 30, op="+")
        print(f"Calculator output: {result}")

    # Test GreetingTool
    greeter = find_tool(tools, "greeting")
    if greeter:
        greeting_msg = greeter.run("Akash")
        print(f"Greeting output: {greeting_msg}")

    # Bonus: Remove a tool
    print("\n--- Managing Registry ---")
    remove_tool(tools, "text")

    # Verify removal
    remaining_names = [tool.name for tool in tools]
    print(f"Active tools after removal: {remaining_names}")