# here is the type conversion or type casting in python. It is the process of converting one data type to another data type. In python, we can use the built-in functions to perform type casting. Some common type casting functions include:
# 1. int() - converts a value to an integer
# 2. float() - converts a value to a float
# 3. str() - converts a value to a string
# 4. bool() - converts a value to a boolean

# examples of type casting in python

x = 10.5
y = int(x) # converting float to integer
print("The value of y after converting x to integer:", y) # Output: 10

z = str(x) # converting float to string
print("The value of z after converting x to string:", z) # Output: "10.5"

a = bool(x) # converting float to boolean
print("The value of a after converting x to boolean:", a) # Output: True

b = float(y) # converting integer to float
print("The value of b after converting y to float:", b) # Output: 10.0

c = int(z) # converting string to integer
print("The value of c after converting z to integer:", c) # Output: 10

d = bool(0) # converting integer to boolean
print("The value of d after converting 0 to boolean:", d) # Output: False

e = bool(1) # converting integer to boolean
print("The value of e after converting 1 to boolean:", e) # Output: True