# Project to create a directory to store contact information

import os, os.path

#Prompt user for name of directory

print(os.getcwd())

desired_dir = input("Enter directory name: ")

if os.path.isdir(desired_dir):
    print("Directory located")
    os.chdir(desired_dir)
else:
    print("Directory not located")
    directory = input("Enter new directory: ")
    os.mkdir(directory)
    os.chdir(directory)
    print("Your current directory is " + directory)

filename = input("Enter a .txt file name: ")


def info():

    name = input("Enter your full name: ")
    address = input("Enter your street address: ")
    number = input("Enter your phone number: ")

    with open(filename, 'a') as file_object:
        file_object.write("\n" + name + address + number)


def main():

    while True:
        menu = input("Would you like to add a contact? Yes or No ")
        if (menu == "Yes".lower()):
            info()

        elif (menu == "No".lower()):
            f = open(filename, 'r')
            file_contents = f.read()
            print("Thank you for using the contact directory. Here are your contacts: \n" + file_contents)
            break

main()
