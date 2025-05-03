class Multiplier:
    def __init__(self, factor):
        self.factor = factor  

    def __call__(self, value):
        return value * self.factor

multiplier = Multiplier(5)

print(callable(multiplier)) 

result = multiplier(10)
print(f"Result of multiplying 10 by factor 5: {result}")  
