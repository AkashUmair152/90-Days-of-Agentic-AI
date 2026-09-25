# 🔥 Project 2 — User Management

class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}!")

    def is_adult(self):
        return self.age >= 18

    def get_info(self):
        return {
            "name": self.name,
            "email": self.email,
            "age": self.age
        }

# Execution & Testing
if __name__ == "__main__":
    user = User(
        "Akash",
        "akash@example.com",
        29
    )

    user.greet()
    print(user.is_adult())
    print(user.get_info())