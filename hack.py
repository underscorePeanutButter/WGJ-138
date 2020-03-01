import os

class Directory:
    def __init__(self, name, is_locked, password=None):
        self.name = name
        self.contents = []

        self.is_locked = is_locked
        self.password = password

    def access(self):
        if self.is_locked:
            attempted_password = input("Password: ")

            if attempted_password == self.password:
                self.is_locked = False
                print("Access granted.")
            else:
                print("Access denied.")

        else:
            print("This is not a locked directory.")

class File:
    def __init__(self, name, contents, is_locked, password=None):
        self.name = name
        self.contents = contents

        self.is_locked = is_locked
        self.password = password

    def access(self):
        if self.is_locked:
            attempted_password = input("Password: ")

            if attempted_password == self.password:
                self.is_locked = False
                print("Access granted.")
            else:
                print("Access denied.")

        else:
            print("This is not a locked file.")

def clear_screen():
    os.system("cls")

def list_contents():
    for item in current_directory.contents:
        if type(item) == Directory:
            print("D ", end="")
        elif type(item) == File:
            print("F ", end="")

        print(item.name)

def change_directory(directory):
    global current_directory_path

    if directory == "..":
        

    for item in current_directory.contents:
        if item.name == directory:
            if type(item) == Directory:
                current_directory_path += "/" + item.name
                return

    print("That directory does not exist.")

file_system = {}

file_system["/home"] = Directory("home", False)

file_system["/home/test_1"] = Directory("test_1", True, "1234")
file_system["/home"].contents.append(file_system["/home/test_1"])

current_directory_path = "/home"

clear_screen()

while True:
    current_directory = file_system[current_directory_path]

    command = input(str(current_directory_path) + " - $ ").strip()

    if command == "cls":
        clear_screen()

    if command == "ls":
        list_contents()

    if command.startswith("cd"):
        split_command = command.split(" ")
        change_directory(split_command[1])

    print()
