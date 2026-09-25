# 🔥 Project 3 — Basic Tool System 

class CalculatorTool:
    def __init__(self):
        self.name = "calculator"

    def run(self, a, b):
        return a + b

class TextTool:
    def __init__(self):
        self.name = "text"

    def run(self, text):
        return text.upper()