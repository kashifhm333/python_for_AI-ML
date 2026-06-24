# here is the precedence of the operators in Python, from highest to lowest:
# 1. Parentheses `()`
# 2. Exponentiation `**`
# 3. Unary plus and minus `+x`, `-x`
# 4. Multiplication, division, floor division, modulus `*`, `/`, `//`, `%`
# 5. Addition and subtraction `+`, `-`    
# 6. Bitwise shift operators `<<`, `>>`
# 7. Bitwise AND `&`
# 8. Bitwise XOR `^`
# 9. Bitwise OR `|`
# 10. Comparison operators `==`, `!=`, `>`, `<`, `>=`, `<=`
# 11. Identity operators `is`, `is not`
# 12. Membership operators `in`, `not in`
# 13. Logical NOT `not`
# 14. Logical AND `and`
# 15. Logical OR `or`


# examples of operator precedence in Python:
x = 10
y = 5
z = 2
result = x + y * z # multiplication has higher precedence than addition
print("Result of x + y * z:", result) # Output: 20  

result = (x + y) * z # parentheses have the highest precedence
print("Result of (x + y) * z:", result) # Output: 30

result = x ** y * z # exponentiation has higher precedence than multiplication
print("Result of x ** y * z:", result) # Output: 1000000

result = -x + y # unary minus has higher precedence than addition
print("Result of -x + y:", result) # Output: -5

result = x > y and y > z # comparison operators have higher precedence than logical AND
print("Result of x > y and y > z:", result) # Output: True

result = not x > y # logical NOT has higher precedence than comparison operators
print("Result of not x > y:", result) # Output: False
