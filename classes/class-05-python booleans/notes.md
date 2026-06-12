# 🐍 Python Booleans, Arithmetic Operators, and Assignment Operators

## 📌 Introduction to Booleans

A Boolean is a data type that can have only two values:

* `True`
* `False`

Booleans are used to check conditions and make decisions in a program.

---

# 🔹 Greater Than (`>`)

The greater than operator checks if the value on the left is larger than the value on the right.

### Example

```python
print(10 > 5)
```

### Output

```text
True
```

Another example:

```python
print(5 > 10)
```

### Output

```text
False
```

---

# 🔹 Equality Operator (`==`)

The equality operator checks whether two values are equal.

### Example

```python
print(10 == 10)
```

### Output

```text
True
```

Example:

```python
print(10 == 5)
```

### Output

```text
False
```

---

# 🔹 Empty Integer Boolean

The number `0` is considered `False` in Python.

### Example

```python
print(bool(0))
```

### Output

```text
False
```

Any non-zero number is considered `True`.

### Example

```python
print(bool(1))
print(bool(100))
```

### Output

```text
True
True
```

---

# ➕ Arithmetic Operators

Arithmetic operators are used to perform mathematical operations.

| Operator | Description    | Example  |
| -------- | -------------- | -------- |
| `+`      | Addition       | `5 + 3`  |
| `-`      | Subtraction    | `5 - 3`  |
| `*`      | Multiplication | `5 * 3`  |
| `/`      | Division       | `5 / 2`  |
| `//`     | Floor Division | `5 // 2` |
| `%`      | Modulus        | `5 % 2`  |
| `**`     | Exponent       | `5 ** 2` |

---

## Addition

```python
print(5 + 3)
```

Output:

```text
8
```

---

## Subtraction

```python
print(10 - 4)
```

Output:

```text
6
```

---

## Multiplication

```python
print(5 * 4)
```

Output:

```text
20
```

---

## Division

```python
print(10 / 2)
```

Output:

```text
5.0
```

---

## Floor Division

```python
print(5 // 2)
```

Output:

```text
2
```

---

## Modulus

```python
print(5 % 2)
```

Output:

```text
1
```

---

## Exponent

```python
print(5 ** 2)
```

Output:

```text
25
```

---

# 📝 Assignment Operators

Assignment operators are used to assign values to variables.

---

## Basic Assignment (`=`)

```python
x = 10
print(x)
```

Output:

```text
10
```

---

## Add and Assign (`+=`)

```python
x = 10
x += 5

print(x)
```

Output:

```text
15
```

---

## Subtract and Assign (`-=`)

```python
x = 10
x -= 3

print(x)
```

Output:

```text
7
```

---

## Multiply and Assign (`*=`)

```python
x = 5
x *= 2

print(x)
```

Output:

```text
10
```

---

## Divide and Assign (`/=`)

```python
x = 10
x /= 2

print(x)
```

Output:

```text
5.0
```

---

# 🎯 Summary

### Boolean Concepts Covered

* Greater Than (`>`)
* Equality (`==`)
* Empty Integer Boolean (`bool(0)`)

### Arithmetic Operators

* `+` Addition
* `-` Subtraction
* `*` Multiplication
* `/` Division
* `//` Floor Division
* `%` Modulus
* `**` Exponent

### Assignment Operators

* `=`
* `+=`
* `-=`
* `*=`
* `/=`

These are fundamental Python concepts and are used extensively in loops, conditions, functions, automation scripts, and real-world software development.
