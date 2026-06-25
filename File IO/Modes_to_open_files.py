# these are the modes to open files in python:
# 1. "r" - Read mode: It is used to read the content of the file. If the file does not exist, it will raise an error.
# 2. "w" - Write mode: It is used to write content to the file. If the file already exists, it will remove the existing content and write new content to it. If the file does not exist, it will create a new file and write content to it.
# 3. "a" - Append mode: It is used to add new content to the existing content of the file. If the file does not exist, it will create a new file and write content to it.
# 4. "x" - Exclusive creation mode: It is used to create a new file and write content to it. If the file already exists, it will raise an error.
# 5. "b" - Binary mode: It is used to read or write binary files.
# 6. "t" - Text mode: It is used to read or write text files. It is the default mode if we do not specify any mode while opening a file.
# 7. "+" - Update mode: It is used to read and write content to the file. If the file does not exist, it will create a new file and write content to it.

# here we will see how to use these modes to open files in python.

# Read mode
f = open("./Sample Files/sample.txt", "r")
content = f.read()
print(content)
f.close()

# Write mode
f = open("./Sample Files/sample.txt", "w")
f.write("Ronaldo is the best player in the world.\n")
f.close()


# Append mode
f = open("./Sample Files/sample.txt", "a")
f.write("Messi is the second best player in the world.\n")
f.close()


# Exclusive creation mode
f = open("./Sample Files/new_file.txt", "x")
f.write("This is a new file created using exclusive creation mode.\n")
f.close()


# Binary mode
f = open("./Sample Files/sample.txt", "rb")
content = f.read()
print(content)
f.close()


# Text mode
f = open("./Sample Files/sample.txt", "rt")
content = f.read()
print(content)
f.close()

# Update mode
f = open("./Sample Files/sample.txt", "r+")
content = f.read()
print(content)
f.write("This is new content added using update mode.\n")
f.close()


# w+ mode:
f = open("./Sample Files/sample.txt", "w+")
f.write("This is new content added using w+ mode.\n")
f.seek(0)  # Move the file pointer to the beginning of the file
print(f.read())  # It will print the content of the file.
f.close()


