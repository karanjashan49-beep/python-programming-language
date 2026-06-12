# 🔁 Python Loops - Detailed Notes

## 📌 Introduction

In programming, we often need to repeat a block of code multiple times. Instead of writing the same code again and again, we use **loops**.

A loop allows a program to execute a set of instructions repeatedly until a condition is met.

Loops are one of the most important concepts in programming because they help in:

* Reducing code repetition
* Automating repetitive tasks
* Processing large amounts of data efficiently

---

## 🎯 Why We Use Loops

Without loops:

```python id="a1b2c3"
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

With loops:

```python id="a2b3c4"
for i in range(5):
    print("Hello")
```

✔ Cleaner code
✔ Easier to maintain
✔ Less chance of errors

---

## 🔁 Types of Loops in Python

Python has two main types of loops:

1. `for` loop
2. `while` loop

---

# 🔹 1. FOR LOOP

## 📌 Definition

A `for` loop is used when we know **how many times** we want to repeat a block of code.

It is mainly used for iterating over:

* Numbers (range)
* Lists
* Strings
* Collections

---

## 📌 Syntax

```python id="f1g2h3"
for variable in range(start, end):
    # code block
```

---

## 📌 Example 1: Basic for loop

```python id="f2g3h4"
for i in range(5):
    print(i)
```

### Output:

```
0
1
2
3
4
```

---

## 📌 Example 2: Custom range

```python id="f3g4h5"
for i in range(1, 6):
    print(i)
```

---

## 📌 Example 3: Loop through list

```python id="f4g5h6"
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
```

---

## 📌 Example 4: String iteration

```python id="f5g6h7"
for letter in "Python":
    print(letter)
```

---

## ⚠️ Key Points

* `range(n)` runs from `0` to `n-1`
* `for` loop is best when number of iterations is known
* It works with sequences (list, string, tuple)

---

# 🔹 2. WHILE LOOP

## 📌 Definition

A `while` loop is used when we do not know **how many times** the loop will run.

It runs until a condition becomes `False`.

---

## 📌 Syntax

```python id="w1x2y3"
while condition:
    # code block
```

---

## 📌 Example 1: Basic while loop

```python id="w2x3y4"
i = 0

while i < 5:
    print(i)
    i += 1
```

---

## 📌 Output:

```
0
1
2
3
4
```

---

## 📌 Example 2: Countdown

```python id="w3x4y5"
count = 5

while count > 0:
    print(count)
    count -= 1
```

---

## ⚠️ Important Warning

If you forget to update the condition, you may create an **infinite loop**.

Example (wrong):

```python id="w4x5y6"
i = 0
while i < 5:
    print(i)
```

❌ This will run forever because `i` is never updated.

---

# 🔁 LOOP CONTROL STATEMENTS

Python provides special keywords to control loops:

---

## 📌 1. break

Used to stop the loop immediately.

```python id="b1c2d3"
for i in range(10):
    if i == 5:
        break
    print(i)
```

---

## 📌 2. continue

Skips the current iteration and moves to the next one.

```python id="b2c3d4"
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## 📌 3. pass

Does nothing (used as placeholder).

```python id="b3c4d5"
for i in range(5):
    pass
```

---

# 🔁 NESTED LOOPS

A loop inside another loop is called a nested loop.

---

## 📌 Example:

```python id="n1n2n3"
for i in range(3):
    for j in range(2):
        print(i, j)
```

---

## 📌 Output:

```
0 0
0 1
1 0
1 1
2 0
2 1
```

---

# 🧠 REAL-WORLD USES OF LOOPS

Loops are used everywhere in software:

### 💻 Web Applications

* Displaying product lists
* Loading posts on social media

### 📊 Data Processing

* Reading files line by line
* Processing database records

### ⚙️ DevOps & Automation

* Running scripts on multiple servers
* Checking system logs
* Deploying services repeatedly

### 📱 Apps

* Showing notifications
* Handling user input continuously

---

# 🚀 BEST PRACTICES

✔ Always update variables in `while` loop
✔ Avoid infinite loops
✔ Use `for` loop when possible
✔ Keep loops simple and readable
✔ Use meaningful variable names

---

# 🎯 SUMMARY

| Loop Type   | Use Case                   |
| ----------- | -------------------------- |
| for loop    | Known number of iterations |
| while loop  | Condition-based repetition |
| nested loop | Multi-level repetition     |

---

# 📌 FINAL NOTE

Loops are a **foundation of programming logic**.
Once you master loops, you can easily learn:

* Functions
* Arrays / Lists
* Algorithms
* Real-world project development

This is one of the most important steps in your journey toward becoming a developer and DevOps engineer.
