from tools import CalculatorTool, TextTool

calculator = CalculatorTool()
text_tool = TextTool()

print(calculator.name)
print(calculator.run(10, 20))

print(text_tool.name)
print(text_tool.run("hello"))