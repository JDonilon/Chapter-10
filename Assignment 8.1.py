# Project to create a directory to store contact information

import os, os.path

#Prompt user for name of directory

desired_dir = input("Enter directory name: ")

#Directory located
if os.path.isdir(desired_dir):
    print("Directory located")
    os.chdir(desired_dir)
#Directory not found
else:
    print("Directory not located")
    directory = input("Enter new directory: ")
    os.mkdir(directory)
    os.chdir(directory)
    print("Your current directory is " + directory)

#Ask for file name
filename = input("Enter a .txt file name: ")


def verify():
    print("[1] Verify Contact")
    print("[2] Enter information again")

    return int(input("Is this inforamtion correct? "))


#Gather contact information
def info():

    name = input("Enter your full name: ")
    address = input("Enter your street address: ")
    number = input("Enter your phone number: ")
    print(name + ',' + address + ',' + number)
    verify()

    if verify == 1:
        with open(filename, 'a') as file_object:
            file_object.write("\n" + name + ',' + address + ',' + number)
            menu()
    elif verify == 2:
        info()
    else:
        print("That is not an option")
        verify()


#User chooses option
def menu():
    print("Welcome to your Contact List")
    print("[1] Add Contact")
    print("[2] Print Contact List")

    return int(input("Please select a number to continue: "))


def main():

    while True:
        menu_option = menu()
        if menu_option == 1:
            info()

        elif menu_option == 2:
            f = open(filename, 'r')
            file_contents = f.read()
            print("Thank you for using the contact directory. Here are your contacts: \n" + file_contents)
            break
        else:
            print("Please select a menu option")


main()
