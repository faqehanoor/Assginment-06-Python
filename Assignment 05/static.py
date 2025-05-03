class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"

print("Addition:", MathUtils.add(10, 5))
print("Subtraction:", MathUtils.subtract(10, 5))
print("Multiplication:", MathUtils.multiply(10, 5))
print("Division:", MathUtils.divide(10, 5))
print("Division (by zero):", MathUtils.divide(10, 0))
