# Project to create a directory to store contact information

import os, os.path

#Prompt user for name of directory

print(os.getcwd())

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

#Gather contact information
def info():

    name = input("Enter your full name: ")
    address = input("Enter your street address: ")
    number = input("Enter your phone number: ")

    with open(filename, 'a') as file_object:
        file_object.write("\n" + name + address + number)


def main():

    while True:
        menu = input("Would you like to add a contact? Yes or No ")
        if menu == "Yes":
            info()

        elif menu == "No":
            f = open(filename, 'r')
            file_contents = f.read()
            print("Thank you for using the contact directory. Here are your contacts: \n" + file_contents)
            break

main()
