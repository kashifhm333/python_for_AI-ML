# the break and continue statements are used to control the flow of loops in Python.
# here are the examples of break and continue statements in Python:

# example of break statement in while loop
print("Example of break statement:")
count = 0
while count < 5:
    print("Count:", count)
    if count == 3:
        print("Breaking the loop at count =", count)
        break  # this will exit the loop when count is 3
    count += 1
    
# example of continue statement in while loop
print("\nExample of continue statement:")
count = 0
while count < 5:    
    count += 1
    if count == 3:
        print("Skipping the rest of the loop at count =", count)
        continue  # this will skip the rest of the loop when count is 3
    print("Count:", count)
    

