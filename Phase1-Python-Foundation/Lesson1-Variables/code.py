# ============================================
# Lesson 1: Introduction & Variables
# ============================================

# ---- Print Statement ----
print("Hello, World!")
print("Welcome to Python!")

# ---- Variables ----
name = "Hibba"
age = 19
city = "Kahuta"

# ---- Data Types ----
integer_value = 25          # int
float_value = 5.9           # float
string_value = "Python"     # str
boolean_value = True        # bool

print("Integer:", integer_value, "| Type:", type(integer_value))
print("Float:", float_value, "| Type:", type(float_value))
print("String:", string_value, "| Type:", type(string_value))
print("Boolean:", boolean_value, "| Type:", type(boolean_value))

# ---- Basic Operators ----
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# ---- input() Function ----
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

print("Hello,", user_name, "! You are", user_age, "years old.")

# ---- Type Conversion Example ----
user_age_int = int(user_age)
print("Next year you will be:", user_age_int + 1)
