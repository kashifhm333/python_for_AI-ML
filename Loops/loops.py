# while loop

count = 0
while count < 5:
    print("Count:", count)
    count += 1  # increment the count by 1
    
    

# table of 2 using while loop

a= 1
while a <= 10:
    print(a*2)
    a += 1
    



# for loop

st= "hello"
for char in st:
    print(char)


if "o" in st:
    print("o is present in the string")

for i in range(5):
    print(i)  # prints numbers from 0 to 4
    
for i in range(1, 11):
    print(i)  # prints numbers from 1 to 10
    
    
    
word = "artifical intelligence"
count = 0
for char in word:
    if(char=='i'):
        count += 1
print("Number of i's in the word:", count)





# vowels in a word

vo = ["a", "e", "i", "o", "u"]
word = "artificial intelligence"
ct = 0


for ch in word:
    if(ch in vo):
        ct += 1
        print(ch)
print("Number of vowels in the word:", ct)



# range in python

for i in range(10):
    print(i)  # prints numbers from 0 to 9
    
for i in range(1, 11):
    print(i)  # prints numbers from 1 to 10

for i in range(1, 11, 2):
    print(i)  # prints odd numbers from 1 to 10




# sum of n numbers

n = int(input("Enter a number: "))
total=0
for i in range(1,n+1):
    total += i
print("Sum of first", n, "numbers is:", total)