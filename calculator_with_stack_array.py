class Calculator:
    def __init__(self):
        self.history = []   # stores all calculations

    def precedence(self, op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    def apply_operator(self, operators, operands, steps):
        if len(operands) < 2:
            raise ValueError("Invalid expression")

        right = operands.pop()
        left = operands.pop()
        op = operators.pop()

        if op == '+':
            result = left + right
        elif op == '-':
            result = left - right
        elif op == '*':
            result = left * right
        elif op == '/':
            if right == 0:
                raise ZeroDivisionError("Division by zero")
            result = left / right

        steps.append(f"{left} {op} {right} = {result}")
        operands.append(result)

    def evaluate(self, expression):
        operands = []
        operators = []
        steps = []

        tokens = expression.split()

        for token in tokens:
            try:
                operands.append(float(token))
            except ValueError:
                while (operators and
                       self.precedence(operators[-1]) >= self.precedence(token)):
                    self.apply_operator(operators, operands, steps)
                operators.append(token)

        while operators:
            self.apply_operator(operators, operands, steps)

        self.history.append({
            "expression": expression,
            "result": operands[0],
            "steps": steps
        })

        return operands[0]

    def show_history(self):
        if not self.history:
            print("No history available.")
            return

        for i, record in enumerate(self.history, 1):
            print(f"\nCalculation {i}: {record['expression']}")
            for step in record['steps']:
                print(" ", step)
            print(" Result:", record['result'])
def Menu():
    calc = Calculator()

    while True:
        print("\n--- Calculator Menu ---")
        print("1. Evaluate Expression")
        print("2. Show History")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input!")
            continue

        if choice == 1:
            expression = input("Enter expression (space separated): ")
            try:
                result = calc.evaluate(expression)
                print("Result:", result)
            except Exception as e:
                print("Error:", e)

        elif choice == 2:
            calc.show_history()

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

def main():
    Menu()

if __name__ == "__main__":
    main()