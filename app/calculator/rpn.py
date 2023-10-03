class Calculator:
    OPERATORS = ["+", "-", "*", "/"]

    def __init__(self):
        self.element_list = []

    def get_elements(self):
        return self.element_list

    def add_operand(self, operand: float):
        if len(self.element_list) == 2:
            raise ValueError("An operator must follow two operands")
        self.element_list.append(operand)

    def remove_last(self):
        if len(self.element_list) == 0:
            raise ValueError("No operand to remove")
        self.element_list = self.element_list[:-1]

    def clean_stack(self):
        self.element_list = []

    def calculate(self, operator: str) -> float:
        if operator not in Calculator.OPERATORS:
            raise ValueError("unknown operator")
        if len(self.get_elements()) < 2:
            raise ValueError("at least two operands must precede an operator")
        first, second = self.get_elements()[-2:]
        result = first
        if operator == "+":
            result = first + second
        elif operator == "-":
            result = first - second
        elif operator == "*":
            result = first * second
        elif operator == "/":
            result = first / second
        self.element_list = [result]
        return result

    def __str__(self):
        return str(self.element_list)
