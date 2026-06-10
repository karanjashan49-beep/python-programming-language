# Loops in Python

## What is a Loop?

A loop is used in programming to repeat a block of code multiple times until a condition is met.

Instead of writing the same code again and again, we use loops.

---

## Types of Loops in Python

### 1. for loop

A `for` loop is used when we know the number of iterations in advance.

#### Syntax:

```python
for variable in range(start, end):
    # code block
```

#### Example:

```python
for i in range(5):
    print(i)
```

Output:

```
0
1
2
3
4
```

---

### 2. while loop

A `while` loop is used when we don't know the number of iterations in advance.

#### Syntax:

```python
while condition:
    # code block
```

#### Example:

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

Output:

```
0
1
2
3
4
```

---

## Important Points

* Loops help reduce code repetition
* Be careful with `while` loops to avoid infinite loops
* `for` loop is best for fixed iterations
* `while` loop is best for condition-based repetition
