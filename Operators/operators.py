# there are operators in python which are used to perform operations on variables and values. Python divides the operators in the following groups:
# 1. Arithmetic operators
# 2. Assignment operators
# 3. Comparison operators
# 4. Logical operators
# 5. Identity operators
# 6. Membership operators
# 7. Bitwise operators

#                   example of arithmetic operators


x = 10
y = 5

print(x, "+", y, "=", x + y) # addition
print(x, "-", y, "=", x - y) # subtraction
print(x, "*", y, "=", x * y) # multiplication
print(x, "/", y, "=", x / y) # division
print(x, "%", y, "=", x % y) # modulus
print(x, "**", y, "=", x ** y) # exponentiation
print(x, "//", y, "=", x // y) # floor division



#                   examples of assignment operators
print("\nAssignment operators:")
a = 10
a += 5 # a = a + 5
print(a, "after += 5:", a)

a -= 3 # a = a - 3
print(a, "after -= 3:", a)

a *= 2 # a = a * 2
print(a," after *= 2:", a)

a /= 4 # a = a / 4
print(a, "after /= 4:", a)

a %= 3 # a = a % 3
print(a, "after %= 3:", a)

a **= 2 # a = a ** 2
print(a, "after **= 2:", a)

a //= 3 # a = a // 3
print(a, "after //= 3:", a)


#                   examples of comparison operators
print("\nComparison operators:")
x = 10
y = 5
print(x, "==", y, ":", x == y) # equal to
print(x, "!=", y, ":", x != y) # not equal to
print(x, ">", y, ":", x > y) # greater than
print(x, "<", y, ":", x < y) # less than
print(x, ">=", y, ":", x >= y) # greater than or equal to
print(x, "<=", y, ":", x <= y) # less than or equal to


# examples of logical operators
print("\nLogical operators:")
x = True
y = False
print(x, "and", y, ":", x and y) # logical AND
print(x, "or", y, ":", x or y) # logical OR
print("not", x, ":", not x) # logical NOT
print(not (6>4))  #it is false





#                   examples of identity operators
print("\nIdentity operators:")
x = 10
y = 10
print(x, "is", y, ":", x is y) # identity operator
print(x, "is not", y, ":", x is not y) # identity operator


# examples of membership operators
print("\nMembership operators:")
x = "Hello"
print("H" in x, ":", "H" in x) # membership operator
print("h" in x, ":", "h" in x) # membership operator
print("Hello" not in x, ":", "Hello" not in x) # membership operator
print("World" not in x, ":", "World" not in x) # membership operator


# examples of bitwise operators
print("\nBitwise operators:")
x = 5 # in binary: 0101
y = 3 # in binary: 0011
print(x, "&", y, ":", x & y) # bitwise AND

#   0 1 0 1  (x = 5)
# & 0 0 1 1  (y = 3)
#   -------
#   0 0 0 1  (Result = 1)

print(x, "|", y, ":", x | y) # bitwise OR

#   0 1 0 1  (x = 5)
# | 0 0 1 1  (y = 3)
#   -------
#   0 1 1 1  (Result = 7)

print(x, "^", y, ":", x ^ y) # bitwise XOR

#   0 1 0 1  (x = 5)
# ^ 0 0 1 1  (y = 3)
#   -------
#   0 1 1 0  (Result = 6)

print("~", x, ":", ~x) # bitwise NOT
# ~ 0 1 0 1  (x = 5)
#   -------
#   1 0 1 0  (Result = -6) in two's complement representation

print(x, "<<", 1, ":", x << 1) # bitwise left shift
#   0 1 0 1  (x = 5)
# << 1
#   -------
#   1 0 1 0  (Result = 10)
print(x, ">>", 1, ":", x >> 1) # bitwise right shift
#   0 1 0 1  (x = 5)
# >> 1
#   -------
#   0 0 1 0  (Result = 2)


# we can also use parentheses to change the order of operations in an expression
print("\nOrder of operations:")
x = 10
y = 5
z = 2
print(x, "+", y, "*", z, "=", x + y * z) # without parentheses, multiplication is performed before addition
print("(", x, "+", y, ")", "*", z, "=", (x + y) * z) # with parentheses, addition is performed before multiplication    

