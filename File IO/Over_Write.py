# if we use only "Write" mode, it will remove the existing content of the file and write new content to it. If we want to add new content without removing the existing content.

f = open("./Sample Files/sample.txt", "w")

f.write("Ronaldo is the best player in the world.\n")

f.close()

f = open("./Sample Files/sample.txt", "r")
content = f.readlines()
print(content)  # It will print all lines of the file
f.close()