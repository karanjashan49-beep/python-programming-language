
# Sorting in Python - Examples

## Example 1: Sorting Numbers

``` python
numbers = [10, 5, 8, 2, 1]

numbers.sort()

print(numbers)
```

Output:

    [1, 2, 5, 8, 10]

------------------------------------------------------------------------

## Example 2: Sorting in Descending Order

``` python
numbers = [10, 5, 8, 2, 1]

numbers.sort(reverse=True)

print(numbers)
```

Output:

    [10, 8, 5, 2, 1]

------------------------------------------------------------------------

## Example 3: Using sorted()

``` python
marks = [75, 90, 65, 88]

result = sorted(marks)

print(result)
```

Output:

    [65, 75, 88, 90]

------------------------------------------------------------------------

## Example 4: Sorting Strings

``` python
names = ["Karan", "Aman", "John", "David"]

names.sort()

print(names)
```

Output:

    ['Aman', 'David', 'John', 'Karan']

------------------------------------------------------------------------

## Example 5: Sort Using key()

``` python
words = ["python", "ai", "developer", "code"]

words.sort(key=len)

print(words)
```

Output:

    ['ai', 'code', 'python', 'developer']

------------------------------------------------------------------------

## Example 6: Sorting Tuples

``` python
students = [
    ("Karan", 85),
    ("Aman", 95),
    ("John", 75)
]

students.sort(key=lambda x: x[1])

print(students)
```

Output:

    [('John', 75), ('Karan', 85), ('Aman', 95)]

------------------------------------------------------------------------

## Summary

-   `sort()` changes the original list.
-   `sorted()` creates a new sorted list.
-   `reverse=True` sorts in descending order.
-   `key` helps create custom sorting rules.
