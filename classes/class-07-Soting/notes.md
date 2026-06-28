
# Sorting in Python - Notes

## What is Sorting?

Sorting means arranging data in a particular order.

Examples: - Ascending: 1, 2, 3, 4 - Descending: 4, 3, 2, 1

------------------------------------------------------------------------

## Python Sorting Methods

### 1. sort()

-   Used with lists only.
-   Changes the original list.
-   Returns `None`.

Example:

``` python
numbers = [5, 2, 8, 1]

numbers.sort()

print(numbers)
```

Output:

    [1, 2, 5, 8]

------------------------------------------------------------------------

### 2. sorted()

-   Works with any iterable.
-   Creates a new sorted list.
-   Original data remains unchanged.

Example:

``` python
numbers = [5, 2, 8, 1]

new_list = sorted(numbers)

print(new_list)
```

Output:

    [1, 2, 5, 8]

------------------------------------------------------------------------

## Descending Sorting

Use:

``` python
reverse=True
```

Example:

``` python
numbers.sort(reverse=True)
```

Output:

    [8, 5, 2, 1]

------------------------------------------------------------------------

## Sorting Strings

Python sorts strings alphabetically.

Example:

``` python
names = ["John", "Aman", "Karan"]

names.sort()

print(names)
```

Output:

    ['Aman', 'John', 'Karan']

------------------------------------------------------------------------

## Custom Sorting with key

The `key` parameter defines how sorting should happen.

Example:

``` python
words = ["python", "ai", "developer"]

words.sort(key=len)

print(words)
```

Output:

    ['ai', 'python', 'developer']

------------------------------------------------------------------------

## Lambda with Sorting

Example:

``` python
students = [
    ("Aman", 90),
    ("Karan", 80),
    ("John", 70)
]

students.sort(key=lambda x: x[1])
```

Sorting is based on marks.

------------------------------------------------------------------------

## Difference Between sort() and sorted()

  sort()                      sorted()
  --------------------------- -------------------------------------
  Only lists                  Any iterable
  Changes original list       Creates new list
  Faster for modifying list   Better when original data is needed

------------------------------------------------------------------------

## Time Complexity

Python uses Timsort algorithm.

Average:

    O(n log n)

------------------------------------------------------------------------

## Important Points

-   Use `sort()` when you want to modify a list.
-   Use `sorted()` when you need a new sorted result.
-   Use `key` for custom sorting rules.
-   Use `reverse=True` for descending order.
