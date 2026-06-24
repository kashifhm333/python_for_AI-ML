marks= [23, 46, 53, 43, 23, 45, 56, 67, 78, 89, 90]

print(marks[0]) # it will print the first element of the list
print(marks[1]) # it will print the second element of the list
print(marks[2]) # it will print the third element of the list
print(marks[3]) # it will print the fourth element of the list

for i in range(len(marks)):
    print(marks[i])


print(marks[-1]) # it will print the last element of the list
print(marks[-2]) # it will print the second last element of the list


print(marks[0:5]) # it will print the first 5 elements of the list
print(marks[5:]) # it will print the elements of the list from index 5 to the end of the list
print(marks[:5]) # it will print the




# how to change the value of an element in the list
marks[0] = 100
for i in range(len(marks)):
    print(marks[i])


# how to add an element to the list
marks.append(99)
for i in range(len(marks)):
    print(marks[i])
    
    
# how to add an element at a specific index in the list
marks.insert(2, 88) # it will insert the element 88 at index 2 in the list
for i in range(len(marks)):
    print(marks[i])
    
# how to remove an element from the list
marks.remove(23) # it will remove the first occurrence of the element 23 from the list
for i in range(len(marks)):
    print(marks[i])
    

# how to sort the list
marks.sort()
for i in range(len(marks)):
    print(marks[i])
    
# how to reverse the list
marks.reverse()
for i in range(len(marks)):
    print(marks[i])


# how to find the length of the list
print(len(marks)) # it will print the length of the list


# how to find the index of an element in the list
print(marks.index(45)) # it will print the index of the first occurrence of the

# how to count the number of occurrences of an element in the list
print(marks.count(23)) # it will print the number of occurrences of the element 23 in the list



# how to clear the list
marks.clear()
print(marks) # it will print an empty list