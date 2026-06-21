# Python Operator Precedence

Operator precedence determines the order in which operators are evaluated in an expression when multiple operators appear together. Operators with **higher precedence** are evaluated **before** operators with **lower precedence**.

The table below lists Python operators from **highest precedence (top)** to **lowest precedence (bottom)**, as defined in the official Python documentation.

| Precedence | Operator | Description |
|---|---|---|
| 1 (Highest) | `(expressions...)`, `[expressions...]`, `{key: value...}`, `{expressions...}` | Parenthesized expression, list/dict/set display |
| 2 | `x[index]`, `x[index:index]`, `x(arguments...)`, `x.attribute` | Subscription, slicing, call, attribute reference |
| 3 | `await x` | Await expression |
| 4 | `**` | Exponentiation (binds less tightly on the left, more tightly on the right, e.g. `2**3**2 = 2**(3**2)`) |
| 5 | `+x`, `-x`, `~x` | Unary plus, unary minus, bitwise NOT |
| 6 | `*`, `@`, `/`, `//`, `%` | Multiplication, matrix multiplication, division, floor division, remainder |
| 7 | `+`, `-` | Addition, subtraction |
| 8 | `<<`, `>>` | Bitwise left shift, right shift |
| 9 | `&` | Bitwise AND |
| 10 | `^` | Bitwise XOR |
| 11 | `\|` | Bitwise OR |
| 12 | `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==` | Comparisons, including membership and identity tests |
| 13 | `not x` | Boolean NOT |
| 14 | `and` | Boolean AND |
| 15 | `or` | Boolean OR |
| 16 | `if – else` | Conditional expression (ternary) |
| 17 | `lambda` | Lambda expression |
| 18 (Lowest) | `:=` | Assignment expression (walrus operator) |

## Notes

- Operators in the **same row** of the table have **equal precedence**. When operators have equal precedence, evaluation follows their **associativity** (usually left-to-right, except `**` which is right-to-left).
- **Parentheses `()`** can always be used to override default precedence and force a specific evaluation order — they have the highest effective precedence.
- The **exponentiation operator `**`** is right-associative: `2 ** 3 ** 2` evaluates as `2 ** (3 ** 2)` = `512`, not `(2 ** 3) ** 2` = `64`.
- **Comparison operators** (`<`, `>`, `==`, etc.) can be chained: `a < b < c` is equivalent to `a < b and b < c`.

## Examples

```python
# Multiplication before addition
result = 2 + 3 * 4        # 14, not 20

# Exponent before unary minus
result = -2 ** 2           # -4, because ** binds tighter than unary -

# Parentheses override precedence
result = (2 + 3) * 4       # 20

# 'and' before 'or'
result = True or False and False   # True, since 'and' evaluates first

# Comparison before boolean operators
result = 5 > 3 and 2 < 4   # True

# Right-to-left associativity of **
result = 2 ** 3 ** 2       # 512 -> 2 ** (3 ** 2)
```
