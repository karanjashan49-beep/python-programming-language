# Python Operators - Complete Guide

## 📌 Introduction

Operators are special symbols in Python used to perform operations on variables and values. Python provides several types of operators that help in mathematical calculations, comparisons, logical decisions, and more.

---

# 1. Arithmetic Operators

Used to perform mathematical operations.

| Operator | Description    | Example  | Output |
| -------- | -------------- | -------- | ------ |
| `+`      | Addition       | `5 + 3`  | `8`    |
| `-`      | Subtraction    | `5 - 3`  | `2`    |
| `*`      | Multiplication | `5 * 3`  | `15`   |
| `/`      | Division       | `5 / 2`  | `2.5`  |
| `//`     | Floor Division | `5 // 2` | `2`    |
| `%`      | Modulus        | `5 % 2`  | `1`    |
| `**`     | Exponentiation | `5 ** 2` | `25`   |

### Example

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

---

# 2. Comparison Operators

Used to compare values.

| Operator | Description              |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

### Example

```python
x = 10
y = 20

print(x == y)
print(x != y)
print(x > y)
print(x < y)
```

---

# 3. Assignment Operators

Used to assign values to variables.

| Operator | Example   |
| -------- | --------- |
| `=`      | `x = 5`   |
| `+=`     | `x += 2`  |
| `-=`     | `x -= 2`  |
| `*=`     | `x *= 2`  |
| `/=`     | `x /= 2`  |
| `//=`    | `x //= 2` |
| `%=`     | `x %= 2`  |
| `**=`    | `x **= 2` |

### Example

```python
x = 10
x += 5

print(x)
```

---

# 4. Logical Operators

Used to combine conditional statements.

| Operator | Description                              |
| -------- | ---------------------------------------- |
| `and`    | Returns True if both conditions are True |
| `or`     | Returns True if one condition is True    |
| `not`    | Reverses the result                      |

### Example

```python
a = True
b = False

print(a and b)
print(a or b)
print(not a)
```

---

# 5. Bitwise Operators

Operate on binary numbers.

| Operator | Description |    |
| -------- | ----------- | -- |
| `&`      | AND         |    |
| `        | `           | OR |
| `^`      | XOR         |    |
| `~`      | NOT         |    |
| `<<`     | Left Shift  |    |
| `>>`     | Right Shift |    |

### Example

```python
a = 6
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)
```

---

# 6. Identity Operators

Used to compare memory locations.

| Operator | Description                   |
| -------- | ----------------------------- |
| `is`     | True if objects are the same  |
| `is not` | True if objects are different |

### Example

```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)
print(x is z)
print(x is not z)
```

---

# 7. Membership Operators

Used to check whether a value exists in a sequence.

| Operator | Description          |
| -------- | -------------------- |
| `in`     | Value exists         |
| `not in` | Value does not exist |

### Example

```python
languages = ["Python", "Java", "C++"]

print("Python" in languages)
print("Go" not in languages)
```

---

# 8. Unary Operators

Operate on a single operand.

### Example

```python
x = 10

print(+x)
print(-x)
```

---

# 9. Operator Precedence

Python follows a specific order when evaluating expressions.

| Priority | Operators            |   |
| -------- | -------------------- | - |
| Highest  | `()`                 |   |
|          | `**`                 |   |
|          | `+x`, `-x`, `~x`     |   |
|          | `*`, `/`, `//`, `%`  |   |
|          | `+`, `-`             |   |
|          | `<<`, `>>`           |   |
|          | `&`                  |   |
|          | `^`                  |   |
|          | `                    | ` |
|          | Comparison Operators |   |
|          | `not`                |   |
|          | `and`                |   |
| Lowest   | `or`                 |   |

### Example

```python
result = 5 + 2 * 3
print(result)
```

Output:

```text
11
```

---

# 🎯 Key Takeaways

* Arithmetic operators perform calculations.
* Comparison operators compare values.
* Assignment operators update variables.
* Logical operators combine conditions.
* Bitwise operators work with binary data.
* Identity operators compare object references.
* Membership operators check existence in collections.
* Understanding operator precedence helps avoid unexpected results.

---

## Author

Created as part of a Python learning journey and GitHub portfolio project.
