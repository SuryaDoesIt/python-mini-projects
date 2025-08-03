import os

print('press 1 for creating a file')
print('press 2 for reading a file ')
print('press 3 for updating a file')
print('press 4 for deleting a file')

try:
    check = int(input('enter your choice :) --> ')) #it catches invalid type
    print("YOU CHOSE THE WRONG INPUT")
    exit()
except:
    print("YOU CHOSE THE WRONG INPUT")
    exit()
    
# Creating a file
if check == 1:
    name = input('What is the name of the file you want to create? ')
    try:
        with open(name, 'w') as f:
            print("FILE CREATED SUCCESSFULLY")
    except:
        print("SOME ERROR OCCURRED WHILE CREATING THE FILE")

# Reading a file
elif check == 2:
    choose = input("Write the name of the file you want to read (exact name): ")
    try:
        with open(choose, "r") as f:
            content = f.read()
            print("FILE ACCESSED SUCCESSFULLY, BELOW IS THE CONTENT:)")
            print(content)
    except:
        print(f"NO '{choose}' FILE FOUND !!")

# Updating a file
elif check == 3:
    file = input("Choose the file you want to add the new text to: ")
    update = input(f"What do you want to add in the '{file}' file? ")
    try:
        with open(file, 'w') as r:
            r.write(update)
        print("FILE UPDATED SUCCESSFULLY")
    except:
        print("SOME ERROR OCCURRED, PLEASE TRY AGAIN :<")

# To Delete a file
elif check == 4:
    name = input('WRITE THE NAME OF THE FILE YOU WANT TO DELETE: ')
    try:
        os.remove(name)
        print(f"File '{name}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{name}' not found.")
    except:
        print("SOME ERROR OCCURRED WHILE DELETING THE FILE")

# if there is an Invalid input
else:
    print("INVALID CHOICE. PLEASE SELECT BETWEEN 1 TO 4.")
