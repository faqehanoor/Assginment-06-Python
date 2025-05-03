class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age is below the required minimum of 18")
    else:
        return "Age is valid"
    
try:
    age = int(input("Enter your age: "))
    print(check_age(age))
except InvalidAgeError as e:
    print(f"Error: {e}")

