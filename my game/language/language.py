class Interpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line.startswith("PRINT"):
                    _, value = line.split(" ", 1)
                    print(self.evaluate_expression(value))
                elif "=" in line:
                    var, exp = line.split("=")
                    self.variables[var.strip()] = self.evaluate_expression(exp)

    def evaluate_expression(self, exp):
        tokens = exp.split()
        if len(tokens) == 1:
            # Single value
            if tokens[0].isdigit():
                return int(tokens[0])
            elif tokens[0] in self.variables:
                return self.variables[tokens[0]]
        else:
            # Binary expression
            left = self.evaluate_expression(tokens[0])
            right = self.evaluate_expression(tokens[2])
            operator = tokens[1]
            if operator == "+":
                return left + right
            elif operator == "-":
                return left - right
            elif operator == "*":
                return left * right
            elif operator == "/":
                return left / right

if __name__ == "__main__":
    interpreter = Interpreter()
    filename = input("Enter the filename: ")
    interpreter.interpret(filename)
