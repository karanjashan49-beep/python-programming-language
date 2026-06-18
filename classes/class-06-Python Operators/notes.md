# Python Operators - Notes

## What are Operators?

Operators are special symbols used to perform operations on variables and values in Python.

Example:

```python
a = 10
b = 5

print(a + b)
```

Output:

```text
15
```

---

# Types of Operators in Python

Python provides seven major categories of operators:

1. Arithmetic Operators
2. Comparison Operators
3. Assignment Operators
4. Logical Operators
5. Bitwise Operators
6. Identity Operators
7. Membership Operators

---

# 1. Arithmetic Operators

Used for mathematical calculations.

| Operator | Meaning        |
| -------- | -------------- |
| +        | Addition       |
| -        | Subtraction    |
| *        | Multiplication |
| /        | Division       |
| //       | Floor Division |
| %        | Modulus        |
| **       | Exponentiation |

### Important Notes

* `/` always returns a float value.
* `//` removes the decimal portion.
* `%` returns the remainder.
* `**` is used for powers.

Example:

```python
5 / 2   # 2.5
5 // 2  # 2
5 % 2   # 1
5 ** 2  # 25
```

---

# 2. Comparison Operators

Used to compare two values.

Result is always:

```python
True
```

or

```python
False
```

Operators:

```python
==
!=
>
<
>=
<=
```

Example:

```python
10 > 5
```

Output:

```python
True
```

---

# 3. Assignment Operators

Used to assign values to variables.

Basic assignment:

```python
x = 10
```

Shortcut assignments:

```python
x += 5
x -= 5
x *= 5
x /= 5
x //= 5
x %= 5
x **= 5
```

Benefits:

* Cleaner code
* Faster to write
* Commonly used in loops

---

# 4. Logical Operators

Used to combine conditions.

### and

Returns True only when all conditions are True.

```python
True and True
```

Output:

```python
True
```

### or

Returns True if at least one condition is True.

```python
True or False
```

Output:

```python
True
```

### not

Reverses the result.

```python
not True
```

Output:

```python
False
```

---

# 5. Bitwise Operators

Work directly on binary values.

Operators:

```python
&
|
^
~
<<
>>
```

Interview Tip:

Before using bitwise operators, convert numbers to binary.

Example:

```python
6 = 110
3 = 011

6 & 3 = 010
```

Output:

```python
2
```

---

# 6. Identity Operators

Compare memory locations of objects.

Operators:

```python
is
is not
```

Example:

```python
a = [1, 2]
b = a

a is b
```

Output:

```python
True
```

### Important

* `==` compares values.
* `is` compares memory addresses.

Example:

```python
a = [1,2]
b = [1,2]

a == b      # True
a is b      # False
```

---

# 7. Membership Operators

Used to check whether an item exists in a collection.

Operators:

```python
in
not in
```

Example:

```python
"Python" in ["Python", "Java"]
```

Output:

```python
True
```

---

# Operator Precedence

Python evaluates operators according to precedence rules.

Highest to Lowest:

```text
()
**
+x, -x, ~x
*, /, //, %
+, -
<<, >>
&
^
|
Comparison Operators
not
and
or
```

Example:

```python
5 + 2 * 3
```

Output:

```python
11
```

because multiplication executes before addition.

---

# Common Interview Questions

### Difference between / and // ?

```python
5 / 2   # 2.5
5 // 2  # 2
```

---

### Difference between == and is ?

```python
==  → compares values
is  → compares memory locations
```

---

### What does % operator do?

Returns the remainder after division.

```python
10 % 3
```

Output:

```python
1
```

---

### What does ** operator do?

Used for exponentiation.

```python
2 ** 4
```

Output:

```python
16
```

---

# Quick Revision Sheet

```text
+   Addition
-   Subtraction
*   Multiplication
/   Division
//  Floor Division
%   Modulus
**  Power

==  Equal
!=  Not Equal
>   Greater Than
<   Less Than

and Logical AND
or  Logical OR
not Logical NOT

&   Bitwise AND
|   Bitwise OR
^   Bitwise XOR
~   Bitwise NOT

is      Identity
is not  Identity

in      Membership
not in  Membership
```

---

## Summary

Operators are one of the most fundamental concepts in Python. Understanding how they work is essential for writing efficient programs, solving coding challenges, and succeeding in technical interviews.
