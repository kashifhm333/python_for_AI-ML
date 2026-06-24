f = open("./Sample Files/sample.txt", "r")

# data = f.read()
# print(data)
# f.close()


# read Line

data = f.readline()
print(data)     # It will print the first line of the file

data = f.readline()
print(data)     # It will print the second line of the file

# read all lines
data = f.readlines()
print(data)     # It will print all the lines of the file in a list format
f.close()