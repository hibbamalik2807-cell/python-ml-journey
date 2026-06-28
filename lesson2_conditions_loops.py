"""
Lesson 2: Conditions & Loops
------------------------------
This lesson cover two basic concepts:
1. Conditions (if, elif, else)
2. Loops (for, while)
"""

# ---------------------------------------------
# 1. CONDITIONS (if, elif, else)
# ---------------------------------------------

print("---- Conditions Example ----")

age = 20

if age < 13:
    print("You are child.")
elif age < 20:
    print("You are teenager.")
else:
    print("You are adult.")


# Example 2: To check number is even or odd
number = 7

if number % 2 == 0:
    print(f"{number} Number is even.")
else:
    print(f"{number} Number is odd.")


# ---------------------------------------------
# 2. FOR LOOP
# ---------------------------------------------

print("\n---- For Loop Example ----")

# Print numbers from 1 to 5
for i in range(1, 6):
    print("Number:", i)

# Loop within list
fruits = ["Apple", "Banana", "Mango"]
for fruit in fruits:
    print("Fruit:", fruit)


# ---------------------------------------------
# 3. WHILE LOOP
# ---------------------------------------------

print("\n---- While Loop Example ----")

count = 1
while count <= 5:
    print("Count:", count)
    count += 1 


# ---------------------------------------------
# 4. BREAK & CONTINUE
# ---------------------------------------------

print("\n---- Break & Continue Example ----")

# break: breaks the loop
for i in range(1, 10):
    if i == 5:
        print("5 (breaks at this number)")
        break
    print(i)

# continue: skip the specific value
for i in range(1, 6):
    if i == 3:
        continue 
    print("Value:", i)


# ---------------------------------------------
# 5. NESTED LOOP (loop ke andar loop)
# ---------------------------------------------

print("\n---- Nested Loop Example (Multiplication Table) ----")

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("-----")
