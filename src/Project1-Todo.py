import functionsTodo
import os
initChoice = str(input("Please choose - \n 1. To open existing ToDo \n 2. Create a new ToDo")).strip()

match initChoice:
    case "1":
        for f in os.listdir("../data/"):
            print(f)
    case "2":
        print("You have chosen to create a new ToDo list")
    case _:
        print("This is not a valid choice")


