
color = input("Enter the color: ")
match color:
    case "red":
        print("The color is red")
    case "blue":
        print("The color is blue")
    case "green":
        print("The color is green") 
    case "white":
        print("The color is white")
    case "black":
        print("The color is black")
    case "yellow":
        print("The color is yellow")
    case _:
        print("The color is not in the list")