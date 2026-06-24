se = {1,2,3,4,5,6,7,8,9,10}

print(se) 
print(type(se)) # it will print the type of the variable set

# print(se[0]) # it will give an error because sets are unordered and do not support indexing

print(len(se)) # it will print the length of the set
print(5 in se) # it will print True because 5 is an element of the set


se.add(11) # it will add the element 11 to the set
print(se)



empty_set = {}
print(type(empty_set)) # it will print <class 'dict'> because {} creates an empty dictionary, not an empty set


emptyset= set() # this is the correct way to create an empty set
print(type(emptyset)) # it will print <class 'set'> because set) creates


# Method of set
se.remove(5) # it will remove the element 5 from the set
print(se)

se.discard(6) # it will remove the element 6 from the set, but if the element is not present in the set, it will not give an error
print(se)


se.clear() # it will remove all the elements from the set
print(se) # it will print an empty set


se.add(1)
se.add(2)
print(se)


se.pop() # it will remove and return an arbitrary element from the set
print(se) # it will print the set after removing an arbitrary element


se.intersection({2,3,4}) # it will return a new set that contains the common elements between the two sets
print(se) # it will print the original set because the intersection method does not modify the original



se.union({2,3,4}) # it will return a new set that contains all the elements from both sets
print(se) # it will print the original set because the union method does not modify the original





#                       practice on sets

course = {
    ("ronaldo", "maths"),
    ("messi", "physics"),
    ("neymar", "chemistry"),
    ("mbappe", "english")
}


# print(course) # it will print the set of tuples

for tup in course:
    print(tup[0])



for tup in course:
    print(tup[0], tup[1]
)
    
    
    
print("\nthe second way\n")    
for name,subject in course:
    print(name, subject)



print("\nthe third way")
for name, subject in course:
    if(subject == "english"):
        print(name)


print("\nthe fourth way")

for i in course:
    if(i[1]=="maths"):
        print(i[0])