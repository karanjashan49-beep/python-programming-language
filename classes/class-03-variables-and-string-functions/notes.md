# Variables and String Functions

## Variables

A variable is a name that stores a value. You can use the variable later in your program.

```python
name = "Karan"
age = 21
city = "Punjab"
```

In this example:

- `name` stores text
- `age` stores a number
- `city` stores text

## Rules for Variable Names

- Variable names can contain letters, numbers, and underscores.
- Variable names cannot start with a number.
- Variable names should not contain spaces.
- Variable names should be clear and meaningful.

Good examples:

```python
student_name = "Karan"
total_marks = 95
favorite_language = "Python"
```

Bad examples:

```python
2name = "Karan"
student name = "Karan"
```

## Changing Variable Values

You can change the value of a variable.

```python
language = "Python"
print(language)

language = "Java"
print(language)
```

Output:

```text
Python
Java
```

## String Variables

A string is text written inside single quotes or double quotes.

```python
name = "Karan"
course = 'Python'
```

Both are correct.

## Joining Strings

You can join strings using `+`.

```python
first_name = "Karan"
last_name = "Singh"

full_name = first_name + " " + last_name
print(full_name)
```

Output:

```text
Karan Singh
```

## Useful String Functions

Python strings have many useful functions. These functions help you change, search, count, and format text.

## upper()

Converts text to capital letters.

```python
message = "python is easy"
print(message.upper())
```

Output:

```text
PYTHON IS EASY
```

## lower()

Converts text to small letters.

```python
message = "PYTHON IS EASY"
print(message.lower())
```

Output:

```text
python is easy
```

## title()

Converts the first letter of each word to capital.

```python
message = "python programming language"
print(message.title())
```

Output:

```text
Python Programming Language
```

## capitalize()

Converts the first letter of the sentence to capital.

```python
message = "python is easy"
print(message.capitalize())
```

Output:

```text
Python is easy
```

## count()

Counts how many times a word or letter appears.

```python
paragraph = "my car is new and my car is fast"
print(paragraph.count("car"))
```

Output:

```text
2
```

You can also count a single letter.

```python
word = "programming"
print(word.count("m"))
```

Output:

```text
2
```

## Counting Commands

Counting commands help you count letters, words, or characters in a string.

## Count a Word

```python
sentence = "Python is easy and Python is powerful"
print(sentence.count("Python"))
```

Output:

```text
2
```

## Count a Letter

```python
word = "banana"
print(word.count("a"))
```

Output:

```text
3
```

## Count Total Characters

Use `len()` to count total characters, including spaces.

```python
message = "Hello Python"
print(len(message))
```

Output:

```text
12
```

## replace()

Replaces one word with another word.

```python
sentence = "I like Java"
print(sentence.replace("Java", "Python"))
```

Output:

```text
I like Python
```

## find()

Finds the position of a word or letter.

```python
message = "I am learning Python"
print(message.find("Python"))
```

If the word is not found, Python returns `-1`.

## strip()

Removes extra spaces from the beginning and end of a string.

```python
name = "   Karan   "
print(name.strip())
```

Output:

```text
Karan
```

## len()

The `len()` function counts how many characters are in a string.

```python
name = "Karan"
print(len(name))
```

Output:

```text
5
```

## String Slicing

Slicing is used to get a specific part of a string.

Index numbers start from `0`.

```python
language = "Python"

print(language[0])
print(language[1])
print(language[2])
```

Output:

```text
P
y
t
```

## Basic Slicing

```python
language = "Python"
print(language[0:3])
```

Output:

```text
Pyt
```

`0:3` means start from index `0` and stop before index `3`.

## Slice From Start

```python
language = "Python"
print(language[:4])
```

Output:

```text
Pyth
```

## Slice To End

```python
language = "Python"
print(language[2:])
```

Output:

```text
thon
```

## Negative Slicing

Negative indexes count from the end of the string.

```python
language = "Python"
print(language[-1])
print(language[-3:])
```

Output:

```text
n
hon
```

## Complete Practice Example

```python
paragraph = """This is my new car.
My car is very fast.
My car has white colour."""

print(paragraph)
print(paragraph.count("car"))
print(paragraph.replace("My", "Our"))
print(paragraph.upper())

language = "Python"
print(language[0:3])
print(language[-1])
```

## Practice Questions

1. Create a variable called `student_name` and store your name.
2. Create a string and print it in capital letters.
3. Count how many times the word `"Python"` appears in a sentence.
4. Replace `"Java"` with `"Python"` in a sentence.
5. Remove extra spaces from `"   Hello Python   "`.
6. Count how many times the letter `"a"` appears in `"banana"`.
7. Print the first 3 letters of `"Python"`.
8. Print the last letter of `"Python"`.
