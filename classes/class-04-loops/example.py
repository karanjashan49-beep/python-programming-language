# ==========================================================
# Python Loops - Beginner Friendly Examples
# ==========================================================
# This file demonstrates different types of loops in Python
# in a simple and easy way for beginners.
# ==========================================================

print("\n==============================")
print("   PYTHON LOOPS PRACTICE")
print("==============================\n")

# ----------------------------------------------------------
# 1. FOR LOOP (Basic)
# ----------------------------------------------------------
print("1️⃣ FOR LOOP - BASIC")

for i in range(5):
    print("Value of i:", i)

print("\n------------------------------\n")

# ----------------------------------------------------------
# 2. FOR LOOP (Custom Range)
# ----------------------------------------------------------
print("2️⃣ FOR LOOP - CUSTOM RANGE")

for i in range(1, 6):
    print("Number:", i)

print("\n------------------------------\n")

# ----------------------------------------------------------
# 3. WHILE LOOP (Basic)
# ----------------------------------------------------------
print("3️⃣ WHILE LOOP - BASIC")

i = 0

while i < 5:
    print("Value of i:", i)
    i = i + 1

print("\n------------------------------\n")

# ----------------------------------------------------------
# 4. WHILE LOOP (Countdown Example)
# ----------------------------------------------------------
print("4️⃣ WHILE LOOP - COUNTDOWN")

count = 5

while count > 0:
    print("Countdown:", count)
    count = count - 1

print("Blast Off 🚀")

print("\n------------------------------\n")

# ----------------------------------------------------------
# 5. LOOP THROUGH LIST
# ----------------------------------------------------------
print("5️⃣ LOOP THROUGH LIST")

fruits = ["apple", "banana", "mango", "grapes"]

for fruit in fruits:
    print("Fruit:", fruit)

print("\n------------------------------\n")

# ----------------------------------------------------------
# 6. LOOP WITH IF CONDITION (EVEN / ODD)
# ----------------------------------------------------------
print("6️⃣ EVEN OR ODD NUMBERS")

for i in range(10):
    if i % 2 == 0:
        print(i, "is EVEN")
    else:
        print(i, "is ODD")

print("\n------------------------------\n")

# ----------------------------------------------------------
# 7. NESTED LOOP (Loop inside loop)
# ----------------------------------------------------------
print("7️⃣ NESTED LOOP")

for i in range(3):
    for j in range(2):
        print("i =", i, ", j =", j)

print("\n------------------------------\n")

# ----------------------------------------------------------
# 8. LOOP WITH BREAK
# ----------------------------------------------------------
print("8️⃣ BREAK EXAMPLE")

for i in range(10):
    if i == 5:
        print("Stopping loop at", i)
        break
    print("i =", i)

print("\n------------------------------\n")

# ----------------------------------------------------------
# 9. LOOP WITH CONTINUE
# ----------------------------------------------------------
print("9️⃣ CONTINUE EXAMPLE")

for i in range(10):
    if i == 3:
        continue
    print("i =", i)

print("\n------------------------------\n")

# ----------------------------------------------------------
# END OF PROGRAM
# ----------------------------------------------------------
print("✅ LOOP PRACTICE COMPLETED SUCCESSFULLY")
print("Keep practicing to become strong in Python 💪")
