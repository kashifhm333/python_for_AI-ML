intro= "ronaldo is the best football player in the world"

# slicing
print(intro[0:7])
print(intro[11:19]) # it will print the whole string because the end index is greater than the length of the string
print(intro[0:]) # it will print the whole string
print(intro[:]) # it will print the whole string
print(intro[0:7:2]) # it will print every 2nd character
print(intro[::2]) # it will print every 2nd character
print(intro[::3]) # it will print every 3rd character
print(intro[::]) # it will print the whole string

print(intro[7:len(intro)]) # it will print the whole string from index 7 to the end of the string

# negative indexing
print(intro[-1]) # it will print the last character of the string
print(intro[-7:]) # it will print the last 7 characters of the string
print(intro[:-7]) # it will print the string except the last 7 characters
print(intro[-7:-1]) # it will print the last 7 characters of the string except the last character
    