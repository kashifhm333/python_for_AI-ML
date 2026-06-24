tup = (1,3,45, 67, 89, 90, 100)

print(tup)
print(tup[0]) # it will print the first element of the tuple
print(tup[1]) # it will print the second element of the tuple

print("type of tup is: ", type(tup)) # it will print the type of the variable tup

print("length of tup is: ", len(tup)) # it will print the length of the tuple

print(tup[0:3]) # it will print the first 3 elements of the tuple
print(tup[3:6]) # it will print the elements of the tuple from index 3 to index 5



sum = 0
for i in range(len(tup)):
    sum+=tup[i]
print(f"sum of all elements in the tuple is: {sum}") # it will print the sum of all elements in the tuple


new_tup = (1,2,2,3,4,2,5)
print(new_tup.index(2)) # it will print the index of the first occurrence of the element 2 in the tuple


print("the count")


