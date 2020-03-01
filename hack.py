import os

class Directory:
    def __init__(self, name, is_locked, password=None):
        self.name = name
        self.contents = []

        self.is_locked = is_locked
        self.password = password

    def unlock(self):
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

    def unlock(self):
        if self.is_locked:
            attempted_password = input("Password: ")

            if attempted_password == self.password:
                self.is_locked = False
                print("Access granted.")
            else:
                print("Access denied.")

        else:
            print("This is not a locked file.")

class Goal:
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents

        self.is_locked = False

def clear_screen():
    os.system("cls")

def list_contents():
    for item in current_directory.contents:
        if type(item) == Directory:
            print("D", end="")
        elif type(item) == File:
            print("F", end="")

        if item.is_locked:
            print("L ", end="")
        else:
            print("U ", end="")

        print(item.name)

def change_directory(directory):
    global current_directory_path

    if directory == "..":
        split_path = current_directory_path.split("/")

        if len(split_path) <= 2:
            return

        split_path = split_path[1:-1]

        if len(split_path) > 1:
            split_path = "/".join(split_path)
        else:
            split_path = split_path[0]

        split_path = "/" + split_path

        current_directory_path = split_path
        return

    for item in current_directory.contents:
        if item.name == directory:
            if type(item) == Directory:
                if item.is_locked:
                    print("Access denied.")
                    return

                current_directory_path += "/" + item.name
                return

    print("That directory does not exist.")

def read_file(file):
    for item in current_directory.contents:
        if item.name == file:
            if type(item) == File:
                if item.is_locked:
                    print("Access denied.")
                    return

                print(item.contents)
                return

    print("That file does not exist.")

def extract_file(file):
    for item in current_directory.contents:
        if item.name == file:
            if type(item) == Goal:
                level_completed = True

def run():
    global current_directory

    level_completed = False
    clear_screen()

    while True:
        try:
            current_directory = file_system[current_directory_path]

            command = input(str(current_directory_path) + " - $ ").strip()

            if command == "cls":
                clear_screen()

            elif command == "ls":
                list_contents()

            elif command.startswith("cd"):
                split_command = command.split(" ")
                change_directory(split_command[1])

            elif command.startswith("unlock"):
                split_command = command.split(" ")
                file_system[current_directory_path + "/" + split_command[1]].unlock()

            elif command.startswith("read"):
                split_command = command.split(" ")
                read_file(split_command[1])

            elif command.startswith("extract"):
                split_command = command.split(" ")
                extract_file(split_command[1])

            if command == "quit":
                sys.exit()

        except:
            print("Invalid syntax or name. Please try again.")

        print()

        if level_completed:
            return

current_directory = None

# Level 1
file_system = {}
file_system["/home"] = Directory("home", False)
file_system["/home/test_1"] = Directory("test_1", True, "1234")
file_system["/home"].contents.append(file_system["/home/test_1"])
file_system["/home/test_1/password.txt"] = File("password.txt", "The password for test_2 is: 'p.><*as?swor/d'", False)
file_system["/home/test_1"].contents.append(file_system["/home/test_1/password.txt"])
file_system["/home/test_1/test_2"] = Directory("test_2", True, "p.><*as?swor/d")
file_system["/home/test_1"].contents.append(file_system["/home/test_1/test_2"])
current_directory_path = "/home"
run()
