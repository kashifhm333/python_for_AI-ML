# "with" keyword in python is used to wrap the execution of a block of code within methods defined by the context manager. It is commonly used for resource management.

with open("./Sample Files/sample.txt", "r") as f:
    content = f.read()
    print(content)  # It will print the content of the file.