class Tool:
    """Base class for all agentic tools."""
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def run(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement the run() method.")


class CalculatorTool(Tool):
    def __init__(self):
        super().__init__(
            name="calculator",
            description="Performs basic arithmetic addition on two numbers."
        )

    def run(self, a, b):
        return a + b


class WeatherTool(Tool):
    def __init__(self):
        super().__init__(
            name="weather",
            description="Fetches current weather information for a specified city."
        )

    def run(self, city):
        return f"Weather in {city}: 24°C and Sunny"


class SearchTool(Tool):
    def __init__(self):
        super().__init__(
            name="search",
            description="Performs a web search for the given query string."
        )

    def run(self, query):
        return f"Search results for: '{query}'"


# Tool Registry & Execution Test
if __name__ == "__main__":
    # Instantiating tool objects
    tool_registry = [
        CalculatorTool(),
        WeatherTool(),
        SearchTool()
    ]

    print("===== AGENT TOOL REGISTRY =====")
    for tool in tool_registry:
        print(f"Tool Name: {tool.name}")
        print(f"Description: {tool.description}")
        print("-" * 30)

    # Executing tools dynamically
    calc = CalculatorTool()
    print("Calc Output:", calc.run(15, 25))

    weather = WeatherTool()
    print("Weather Output:", weather.run("Lahore"))

    search = SearchTool()
    print("Search Output:", search.run("FastAPI agentic framework"))