class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        super().__init__(message)


def check_age(age):
    if age < 18:
        raise InvalidAgeError()
    else:
        return "Access granted."

print("Program started...")  

try:
    user_age = int(input("Enter your age:"))
    print(check_age(user_age))
except InvalidAgeError as e:
    print("Custom Exception:", e)
except ValueError:
    print("Please enter a valid number.")