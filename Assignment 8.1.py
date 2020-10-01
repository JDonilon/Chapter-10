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

name = input("Enter your full name: ")
address = input("Enter your street address: ")
number = input("Enter your phone number: ")

with open(filename, 'w') as file_object:
    file_object.write(name + "\n" + address + "\n" + number)

print("Would you like to add another contact? ")

with open(filename, 'a') as file_object:
    file_object.write(name + "\n" + address + "\n" + number)