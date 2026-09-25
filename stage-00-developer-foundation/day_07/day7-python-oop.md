# Day 7 — Stage 0: Python Object-Oriented Programming (OOP)

## 1. Day 7 Overview

As applications grow, managing separate variables and functions for every "thing" in your program (users, accounts, tools) becomes messy — imagine tracking `user1_name`, `user1_age`, `user2_name`, `user2_age`... for 1,000 users. **Object-Oriented Programming (OOP)** solves this by letting you group related data and behavior together into a single reusable structure. This matters for your path because as you build FastAPI applications, LLM applications, tools, and agents, many of the "things" you'll model — a user, an agent, a tool, a conversation — naturally combine data and behavior, which is exactly what OOP is designed for.

## 2. What Is OOP?

**Object-Oriented Programming** is a way of organizing code around **objects**, where each object bundles together:
```
Object
├── Data       (attributes)
└── Behavior   (methods)
```
Example — a `User` object might combine:
```
User
├── name
├── email
├── age
│
├── login()
├── logout()
└── send_message()
```
Data: `name`, `email`, `age`. Behavior: `login()`, `logout()`, `send_message()`. The core idea to remember: **an object is a way to keep related state and behavior together.**

## 3. Classes

- **What a class is:** A blueprint that describes what data and behavior objects created from it will have.
- **Class as a blueprint:**
```
Blueprint → House
House blueprint → many actual houses

Class → Object
```
- **Creating a class:**
```python
class User:
    pass
```
This creates the `User` class (the blueprint), but no actual user object exists yet.

## 4. Objects

- **What an object is:** An actual instance created from a class — the "real thing" built from the blueprint.
```python
class User:
    pass

user1 = User()
```
`user1` is an **object** (also called an *instance*) of the `User` class.

- **Multiple objects from one class:** A single class can produce many independent objects.
```python
user1 = User()
user2 = User()
user3 = User()
```

**Remember:**
```
Class  = blueprint
Object = actual thing created from the blueprint
```

## 5. Attributes

- **Object attributes:** Data stored on an object.
```python
class User:
    pass

user1 = User()
user1.name = "Akash"
user1.age = 29
```
```
user1
├── name → "Akash"
└── age  → 29
```
- **Instance attributes:** Attributes specific to one object, typically set via `self` inside `__init__` (see Section 6) — each object can have different values.
- **Class attributes:** Attributes defined directly on the class, generally shared by all objects (covered fully in Section 10).

## 6. `__init__` ⭐⭐⭐

- **What it does:** A special method that runs automatically when a new object is created, used to set up (initialize) that object's starting data.
```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```
- **Why it's used:** Instead of manually assigning attributes one by one after creating each object (`user1.name = "Akash"`), `__init__` lets you pass values directly when creating the object:
```python
user1 = User("Akash", 29)
user2 = User("Ali", 25)
```
- **How it initializes object state:** `self.name = name` stores the given `name` argument onto *this specific object*, so each object ends up with its own independent data:
```
user1 → name: Akash, age: 29
user2 → name: Ali,   age: 25
```

## 7. self

This is usually the most confusing part at first — here's the simplest way to think about it.

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Think of `self` as meaning: **"this particular object."**

When you run `user1 = User("Akash", 29)`, inside the class, `self` refers to `user1`. When you run `user2 = User("Ali", 25)`, `self` refers to `user2` instead. So `self.name = name` means: "store this argument as *this object's* name."

**Mental model:**
```
self
 ↓
"This object"
```
So `self.name` simply means "this object's name."

## 8. Methods

- **What methods are:** Functions defined inside a class — they represent an object's behavior.
```python
class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

user = User("Akash")
user.greet()   # Hello, Akash!
```

- **Methods vs functions:**
```
Function → standalone behavior, not tied to any object
Method   → behavior attached to an object/class
```
```python
def greet(name):              # normal function
    print(f"Hello {name}")

class User:
    def greet(self):          # method
        print(f"Hello {self.name}")
```

- **Methods accessing object state:** A method can read the object's own attributes via `self`, e.g., `self.name` inside `greet()`.

- **Methods changing object state:**
```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

account = BankAccount(1000)
account.deposit(500)
print(account.balance)   # 1500
```

- **Methods returning values:**
```python
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
result = calc.add(10, 20)
print(result)   # 30
```

## 9. Object State

**State** means the current data stored in an object at any given moment.

- **`BankAccount` example:** `account = BankAccount(1000)` → state is `balance = 1000`. After `account.deposit(500)`, state becomes `balance = 1500`.
- **`User` example:** A `User` object's state might be its current `name` and `age`, which can change (e.g., `user.age = 30` updates the state).
- **`Agent` example (conceptual, from the lesson's broader picture):** An `Agent` object might hold state like its `llm` and `tools`, similar in spirit to how agent state was represented as a dictionary in earlier lessons.

```
Object
 ↓
State
 +
Behavior
```

## 10. Class Attributes vs Instance Attributes

| | Instance Attribute | Class Attribute |
|---|---|---|
| **Defined as** | `self.something = value` (usually in `__init__`) | `something = value` directly inside the class body |
| **Value per object** | Can differ between objects | Usually the same/shared across all objects |
| **Example** | `self.name` — `user1.name` = "Akash", `user2.name` = "Ali" | `platform = "MyApp"` — `user1.platform` and `user2.platform` are both "MyApp" |

```python
class User:
    platform = "MyApp"   # class attribute

    def __init__(self, name):
        self.name = name   # instance attribute

user = User("Akash")
print(user.platform)   # MyApp
```

## 11. Inheritance

- **Parent class / child class:** A child class can be built on top of a parent class, inheriting its behavior.
```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass

dog = Dog()
dog.speak()   # Animal sound
```
`Dog` inherited `speak()` from `Animal` without redefining it.

- **Reusing behavior:** Instead of duplicating `eat()`, `sleep()`, `move()` in every animal subclass, they're defined once in `Animal` and reused by `Dog`, `Cat`, etc.

- **Method overriding:** A child class can replace (override) a method it inherited.
```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

dog = Dog()
dog.speak()   # Woof!
```

- **`super()`:** Lets a child class call the parent class's version of a method (commonly used inside `__init__` so the parent still sets up its own attributes).
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

dog = Dog("Buddy", "Labrador")
```
Here, `super().__init__(name)` lets `Animal` set up `self.name`, while `Dog` additionally sets up `self.breed`.

**Remember:**
```
super()
 ↓
Use parent class functionality
```

## 12. Functions vs Classes

- **Use a function** for a simple, standalone action with no ongoing state to track:
```python
def calculate(a, b):
    return a + b

def format_text(text):
    return text.strip().title()

def validate_email(email):
    return "@" in email
```
- **Use a class** when you have data + related behavior + state that need to stay together:
```
BankAccount, User, Agent, Tool, Database connection, Document, Conversation
```
**Important:** Not everything needs to be a class. Agents don't *require* classes — a plain function like `def calculator(a, b): return a + b` is perfectly valid. OOP becomes useful specifically when your application has more complex state and behavior to manage together.

## 13. OOP in Real Applications

Many "things" in a real AI application can naturally be represented as objects/classes:
```
User
Database
Agent
Tool
Message
Conversation
Document
Retriever
LLM
```
Examples:
```python
class User:
    def __init__(self, name):
        self.name = name

class CalculatorTool:
    def run(self, expression):
        ...

class Agent:
    def __init__(self, llm, tools):
        self.llm = llm
        self.tools = tools
```
You don't need to build a full `Agent` class today — this is just showing the shape these ideas will eventually take.

## 14. OOP + Agentic AI

```
Function
   ↓
Tool
   ↓
Class-based Tool
   ↓
State + Behavior
   ↓
Complex AI application
```

A tool built as a plain function works fine for simple cases. But once a tool needs its own data (like a `name`) alongside its behavior (`run()`), a class fits naturally:
```python
class CalculatorTool:
    def __init__(self):
        self.name = "calculator"

    def run(self, a, b):
        return a + b

calculator = CalculatorTool()
calculator.run(10, 20)   # 30
```
Now the tool has:
```
Data     → name = "calculator"
Behavior → run()
```
This is exactly the **data + behavior** model from Section 2, now applied directly to a tool.

## 15. Simple Tool Architecture

```
Tool
├── name
├── description
└── run()
```
A base `Tool` class can define the common shape, and specific tools inherit from it:
```python
class Tool:
    def __init__(self, name):
        self.name = name

    def run(self):
        pass

class CalculatorTool(Tool):
    def run(self, a, b):
        return a + b

calculator = CalculatorTool("calculator")
print(calculator.name)          # calculator
print(calculator.run(10, 20))   # 30
```
Conceptually, `WeatherTool` and `SearchTool` could each inherit from `Tool` the same way, each providing its own `run()` implementation while sharing the common `name` setup — a simplified version of a pattern used in real AI tool frameworks.

## 16. Mental Models

- Class = blueprint.
- Object = actual thing created from the blueprint.
- Attribute = an object's data.
- Method = an object's behavior.
- `self` = "this object."
- `__init__` = set up (initialize) the object.
- Instance attribute = data that can differ per object (`self.x`).
- Class attribute = data usually shared across all objects.
- Inheritance = reuse a parent class's behavior in a child class.
- Method overriding = a child class replaces an inherited method.
- `super()` = call the parent class's version of a method.
- Object = State + Behavior, kept together.
- A function is a standalone action; a method is behavior attached to an object.
- Not every function needs to become a class — use OOP when state and behavior genuinely belong together.
- Tool = name + description + `run()` — a natural fit for a class once a tool needs its own data.

## 17. Common Beginner Mistakes

- **Forgetting `self`** — omitting `self` as the first parameter in a method definition, which causes errors when the method is called.
- **Confusing class and object** — treating the class (`User`) as if it were a specific object, rather than the blueprint objects are created from.
- **Misunderstanding `__init__`** — thinking it must be called manually, when Python calls it automatically when you create an object (e.g., `User("Akash", 29)`).
- **Using a class attribute when an instance attribute is needed** — accidentally sharing a value across all objects when each object actually needed its own independent value.
- **Overusing inheritance** — creating deep or unnecessary parent/child chains for things that don't actually share meaningful behavior.
- **Turning every function into a class** — adding unnecessary complexity when a simple function would do the job just as well.
- **Misunderstanding `super()`** — forgetting to call it in a child's `__init__`, which means the parent's setup code (like setting `self.name`) never runs.

## 18. Practical Code Examples

```python
# Class and object
class User:
    pass

user1 = User()
user1.name = "Akash"

# __init__ and self
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user1 = User("Akash", 29)
user2 = User("Ali", 25)

# Methods
class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

    def is_adult(self):
        return self.age >= 18

# Methods that modify state
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

account = BankAccount("Akash", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())   # 1300

# Class attribute vs instance attribute
class User:
    platform = "MyApp"

    def __init__(self, name):
        self.name = name

# Inheritance and overriding
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("Woof!")

dog = Dog("Buddy", "Labrador")
dog.speak()   # Woof!

# Tool system
class Tool:
    def __init__(self, name):
        self.name = name

    def run(self):
        pass

class CalculatorTool(Tool):
    def run(self, a, b):
        return a + b

class TextTool(Tool):
    def run(self, text):
        return text.upper()

calculator = CalculatorTool("calculator")
text_tool = TextTool("text")

print(calculator.name, calculator.run(10, 20))
print(text_tool.name, text_tool.run("hello"))
```

## 19. Interview Questions

1. **Q: What is OOP?**
   A: A way of organizing code around objects that bundle together data (attributes) and behavior (methods).

2. **Q: What is a class?**
   A: A blueprint that defines what data and behavior objects created from it will have.

3. **Q: What is an object?**
   A: An actual instance created from a class.

4. **Q: What's the difference between a class and an object?**
   A: A class is the blueprint; an object is the real thing built from that blueprint.

5. **Q: What is an attribute?**
   A: Data stored on an object (or class).

6. **Q: What is a method?**
   A: A function defined inside a class, representing an object's behavior.

7. **Q: What does `__init__` do?**
   A: It automatically runs when an object is created, used to set up (initialize) that object's starting attributes.

8. **Q: What does `self` represent?**
   A: "This particular object" — inside a method, it refers to whichever object the method was called on.

9. **Q: What's the difference between an instance attribute and a class attribute?**
   A: An instance attribute (`self.x`) can differ between objects; a class attribute is defined on the class itself and is usually shared by all objects.

10. **Q: What is inheritance?**
    A: A mechanism allowing a child class to reuse behavior defined in a parent class.

11. **Q: What does method overriding mean?**
    A: A child class defining its own version of a method that it inherited, replacing the parent's version.

12. **Q: What does `super()` do?**
    A: Calls the parent class's version of a method — commonly used in `__init__` so the parent's setup logic still runs.

13. **Q: When might a class be better than a simple function?**
    A: When you have data and related behavior that need to be tracked together as state, rather than just a single standalone action.

14. **Q: Does every Python program need OOP?**
    A: No — many things can be built perfectly well with plain functions; OOP is useful specifically when state and behavior belong together.

15. **Q: Explain this code:**
```python
class CalculatorTool:
    def __init__(self):
        self.name = "calculator"

    def run(self, a, b):
        return a + b
```
    A: It defines a `CalculatorTool` class; creating an instance automatically sets its `name` attribute to `"calculator"`, and calling `.run(a, b)` on that instance returns the sum of `a` and `b`.

16. **Q: What's the difference between `calculator(10, 20)` and `calculator.run(10, 20)`, assuming the first is a function and the second is a method?**
    A: `calculator(10, 20)` calls a standalone function directly; `calculator.run(10, 20)` calls a method on a specific object, so it can also access and use that object's own data (`self`).

17. **Q: Explain this architecture:**
```
Tool
 ↓
CalculatorTool
 ↓
run()
```
    A: `Tool` is a base/parent class defining the common shape (like `name` and a `run()` placeholder); `CalculatorTool` inherits from `Tool` and provides its own specific implementation of `run()`.

18. **Q: Why might an Agent object need state?**
    A: Because an agent needs to track information (like its LLM, tools, or ongoing progress) across multiple steps of the agent loop, and object state is exactly the mechanism for holding that information alongside the agent's behavior.

19. **Q: What happens if you forget `self` as the first parameter of a method?**
    A: The method won't correctly receive a reference to the object it's called on, leading to errors when trying to call it normally.

20. **Q: Why is a class attribute like `platform = "MyApp"` typically shared across all objects, unlike `self.name`?**
    A: Because it's defined once on the class itself rather than being set individually per object inside `__init__`, so by default every instance looks up the same shared value.

## 20. Flashcards

Q: What is a class?
A: A blueprint for creating objects.

Q: What is an object?
A: An instance created from a class.

Q: What is an attribute?
A: Data stored on an object.

Q: What is a method?
A: A function defined inside a class.

Q: What does `self` mean?
A: "This object" — a reference to the specific object a method was called on.

Q: What does `__init__` do?
A: Automatically initializes a new object's attributes when it's created.

Q: What is an instance attribute?
A: Data specific to one object, usually set with `self.x` in `__init__`.

Q: What is a class attribute?
A: Data defined on the class itself, generally shared by all objects.

Q: What is inheritance?
A: A child class reusing behavior from a parent class.

Q: What is method overriding?
A: A child class replacing an inherited method with its own version.

Q: What does `super()` do?
A: Calls the parent class's version of a method.

Q: What is "object state"?
A: The current data stored in an object at a given moment.

Q: Can one class create multiple objects?
A: Yes — each with its own independent state.

Q: What's the difference between a function and a method?
A: A function is standalone; a method is behavior attached to an object.

Q: Can a method return a value?
A: Yes, just like a regular function.

Q: Can a method change an object's state?
A: Yes, e.g. `self.balance += amount`.

Q: Does every program need classes?
A: No — simple actions are often better as plain functions.

Q: What does a `Tool` base class commonly define?
A: `name`, `description`, and a `run()` method.

Q: How does `CalculatorTool(Tool)` relate to `Tool`?
A: `CalculatorTool` is a child class that inherits from the `Tool` parent class.

Q: What is a common mistake with `__init__`?
A: Thinking it must be called manually, rather than automatically running when an object is created.

Q: What happens if a child class's `__init__` doesn't call `super().__init__()`?
A: The parent class's setup code (e.g., setting certain attributes) never runs.

Q: Why avoid turning every function into a class?
A: It adds unnecessary complexity when a simple function would work just as well.

Q: What are examples of things that could be represented as classes in an AI app?
A: User, Agent, Tool, Message, Conversation, Document.

Q: Is a plain function-based tool still valid for an agent?
A: Yes — agents don't require classes; OOP is useful, not mandatory.

Q: What's the key idea to remember about objects?
A: An object keeps related state and behavior together.

## 21. Code Output Practice

Predict the output of each snippet (no answers given — verify yourself):

1.
```python
class User:
    def __init__(self, name):
        self.name = name

u = User("Sara")
print(u.name)
```

2.
```python
class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi {self.name}")

u = User("Ali")
u.greet()
```

3.
```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

c = Counter()
c.increment()
c.increment()
print(c.count)
```

4.
```python
class User:
    platform = "MyApp"

u1 = User()
u2 = User()
print(u1.platform, u2.platform)
```

5.
```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

a = Animal()
d = Dog()
a.speak()
d.speak()
```

6.
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Rex", "Labrador")
print(d.name, d.breed)
```

7.
```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

acc = BankAccount(500)
print(acc.withdraw(200))
```

8.
```python
class Tool:
    def __init__(self, name):
        self.name = name

class CalculatorTool(Tool):
    def run(self, a, b):
        return a + b

t = CalculatorTool("calc")
print(t.name)
print(t.run(3, 4))
```

9.
```python
class User:
    def __init__(self, name):
        self.name = name

u1 = User("A")
u2 = User("B")
u1.name = "C"
print(u1.name, u2.name)
```

10.
```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()
```

## 22. Debugging Practice

Each snippet has a bug — identify and fix it:

1.
```python
class User:
    def __init__(name, age):
        self.name = name
        self.age = age
```

2.
```python
class User:
    def __init__(self, name):
        name = name

u = User("Akash")
print(u.name)
```

3.
```python
class User:
    def greet():
        print("Hello")

u = User()
u.greet()
```

4.
```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        balance += amount

acc = BankAccount(100)
acc.deposit(50)
print(acc.balance)
```

5.
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed
```

6.
```python
class Tool:
    def __init__(self, name):
        self.name = name

tool = Tool
print(tool.name)
```

7.
```python
class Calculator:
    def add(self, a, b):
        a + b

calc = Calculator()
result = calc.add(2, 3)
print(result)
```

8.
```python
class User:
    def __init__(self, name):
        self.name = name

u = User("Akash")
print(User.name)
```

9.
```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak():
        print("Woof")

d = Dog()
d.speak()
```

10.
```python
class BankAccount:
    def __init__(self, balance)
        self.balance = balance
```

## 23. Knowledge Test (No Answers)

1. In your own words, explain the difference between a class and an object.
2. Why does `__init__` need `self` as its first parameter?
3. What would happen if you forgot to include `self` when defining a method?
4. Why can two objects of the same class have different values for the same attribute?
5. When is a class attribute more appropriate than an instance attribute, and vice versa?
6. What does it mean for a child class to "override" a method from its parent?
7. Why would a child class call `super().__init__(...)` instead of just writing its own full `__init__` from scratch?
8. Describe, step by step, what happens when you run `user = User("Akash", 29)` for a class with an `__init__` that takes `name` and `age`.
9. Why is a class not automatically "better" than a function — when would a function actually be the more appropriate choice?
10. Scenario: You need to represent a chat conversation that has a growing list of messages and methods to add/retrieve them. Would a function or a class fit better, and why?
11. Scenario: You define `class Tool: name = "generic"` and create two tools without overriding `name` in `__init__`. What would `tool1.name` and `tool2.name` show, and why?
12. Explain how `CalculatorTool(Tool)` relates data and behavior compared to a plain `def calculator(a, b): return a + b` function.
13. Why might an `Agent` class need to store `llm` and `tools` as instance attributes rather than as separate global variables?
14. Scenario: You define a `WeatherTool` and a `SearchTool`, each inheriting from a shared `Tool` base class. What would you expect both to have in common, and what would likely differ?
15. What's the risk of "overusing inheritance," even if a beginner example works fine?
16. Why does the lesson say "not everything needs to be a class"? Give an example of something that's fine as a plain function.
17. If a method modifies `self.balance`, what happens to that value the next time you access `account.balance`?
18. Explain what "object state" means using the `BankAccount` example from today's lesson.
19. Scenario: You accidentally define a class attribute (`self` not used) for something that should differ per object, like a bank balance. What problem would this likely cause?
20. Why is understanding `self`, `__init__`, and inheritance considered foundational before learning frameworks that use classes heavily (as hinted at for future AI tool systems)?

## 24. Five-Minute Revision Sheet

- **Class** = blueprint; **Object** = actual instance created from it.
- **Attribute** = data on an object; **Method** = behavior (a function inside a class).
- **`__init__`** runs automatically when an object is created, to set up its starting attributes.
- **`self`** = "this object" — refers to whichever specific object a method is being called on.
- **Instance attribute** (`self.x`) can differ per object; **class attribute** (defined directly in the class body) is generally shared by all objects.
- **Inheritance:** a child class (`class Dog(Animal):`) reuses a parent class's behavior.
- **Method overriding:** a child class redefines a method it inherited.
- **`super()`:** calls the parent class's version of a method, commonly in `__init__`.
- **Object = State + Behavior**, kept together.
- **Function vs Class:** simple standalone actions → function; data + behavior + state together → class.
- **Tool pattern:** `Tool` base class with `name`, `description`, `run()`; specific tools (`CalculatorTool`, `WeatherTool`) inherit and implement their own `run()`.
- **Key reminder:** Agents don't require classes — OOP is a useful tool, not a requirement.

## 25. What I Must Remember

1. A class is a blueprint; an object is the actual instance created from that blueprint.
2. An object combines data (attributes) and behavior (methods) together.
3. `__init__` automatically runs when an object is created, setting up its initial attributes.
4. `self` refers to "this particular object" inside a class's methods.
5. Instance attributes (`self.x`) can differ between objects; class attributes are generally shared across all objects.
6. A method is just a function defined inside a class, and it can read, change, or return data related to its object.
7. "Object state" means the current data an object holds, which can change over time via its methods.
8. Inheritance lets a child class reuse a parent class's behavior; method overriding lets it replace that behavior.
9. `super()` lets a child class call the parent class's version of a method, commonly to reuse its `__init__` setup.
10. Not every function needs to become a class — use OOP specifically when data, behavior, and state genuinely need to stay together.
11. A `Tool` base class with `name`, `description`, and `run()` is a simple, real pattern for organizing multiple related tools via inheritance.
12. OOP is one useful way to build AI tools and agents, but it is not a requirement — plain functions remain perfectly valid for simpler actions.
