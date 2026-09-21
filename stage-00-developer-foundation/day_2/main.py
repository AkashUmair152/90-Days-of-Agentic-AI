
# Exercise 1 — Age checker

age = 24

if age>= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 🧪 Exercise 2 — Grade calculator

grade = 85

if grade >= 90:
    print("You got an A")
elif grade >= 80:
    print("You got a B")
elif grade >= 70:
    print("You got a C")
elif grade >= 60:
    print("You got a D")
else:
    print("You got an F")


# 🧪 Exercise 3 — Login system

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Invalid username or password")

# 🧪 Exercise 4 — Number loop

# Print numbers:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10 use for and range()

for number in range(1, 11):
    print(number)

# 🧪 Exercise 5 — Even numbers  10
for number in range(11):
    if number % 2 == 0:
        print(f"{number} is even")

# 🧪 Exercise 6 — Process a list

tasks = [
    "Read email",
    "Check weather",
    "Calculate invoice",
    "Send report"
]

for task in tasks:
    print(f"Processing task: {task}")

# 🧪 Exercise 7 — Stop the loop


for number in range(1, 11):
# Print numbers but stop when you reach 6.
    if number == 6:
        break
        print(number)

# 🧪 Exercise 8 — Skip a number skip 4 

numbers = range(1, 11)
for number in numbers:
    if number == 4:
        continue
    print(number)


# 🔥 Day 2 Mini Project

# The user should be able to choose:

# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit

balance = 1000
select_choice = int(input("Please select an option:\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit\n"))
if select_choice == 1:
    print(f"Your balance is: ${balance}")
elif select_choice == 2:
    deposit_amount = float(input("Enter the amount to deposit: "))
    balance += deposit_amount
    print(f"Deposit successful! Your new balance is: ${balance}")
elif select_choice == 3:
    withdraw_amount = float(input("Enter the amount to withdraw: "))
    if withdraw_amount > balance:
        print("Insufficient funds!")
    else:
        balance -= withdraw_amount
        print(f"Withdrawal successful! Your new balance is: ${balance}")
else: 
    print("Exiting the program. Thank you!")