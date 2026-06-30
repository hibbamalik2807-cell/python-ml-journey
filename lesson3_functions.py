# Lesson 3: Functions

# 1. Basic function
def greet():
    print("Hello! Welcome to Python Functions.")
greet()

# 2. Function with parameter
def greet_user(name):
    print(f"Hello, {name}!")
greet_user("Hibba")

# 3. Function with return value
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 3)
print("Sum:", result)

# 4. Default parameter
def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")
greet_with_default()
greet_with_default("Ahmed")

# 5. Function with multiple arguments (*args)
def add_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print("Total:", add_all(1, 2, 3, 4, 5))


# 6. Practical example: Even or Odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"
print(check_even_odd(10))
print(check_even_odd(7))
