import os
import sys
import random

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

    def unlock(self):
        print("This is not a locked file.")

def main_menu():
    while True:
        clear_screen()

        print("------ PeanutButterGames presents ------")
        print("---------- |   |  __   __ | / ----------")
        print("---------- |---| |__| |   |/  ----------")
        print("---------- |   | |  | |__ | \\ ----------")
        print("------- For Weekly Game Jam #138 -------")
        print()
        print("1. 'Story' Mode (work in progress)")
        print("2. 'Random' Mode (currently unavailable)")
        print("3. Quit")
        choice = input("Choice: ")
        print()

        if choice == "1":
            return

        elif choice == "2":
            print("Random mode is still in progress. Please check back in later.")
            wait_for_input()

        elif choice == "3":
            sys.exit()

        else:
            print("That choice is invalid.")
            wait_for_input()

def wait_for_input():
    print()
    input("Press enter to continue...")

def check_completion():
    if level_completed == False:
        sys.exit()

def clear_screen():
    os.system("cls")

def list_contents():
    for item in current_directory.contents:
        if type(item) == Directory:
            print("D", end="")
        elif type(item) == File:
            print("F", end="")
        elif type(item) == Goal:
            print("G", end="")

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
            if type(item) == File or type(item) == Goal:
                if item.is_locked:
                    print("Access denied.")
                    return

                print(item.contents)
                return

    print("That file does not exist.")

def extract_file(file):
    global level_completed

    for item in current_directory.contents:
        if item.name == file:
            if type(item) == Goal:
                level_completed = True
                return

    print("That file doesn't exist or cannot be extracted.")

def show_command_list():
    print("Available Commands:")
    print("  help    - displays this list")
    print("  cls     - clears the screen")
    print("  ls      - lists the contents of the current directory")
    print("  cd      - changes the current directory (syntax: cd <directory name>)")
    print("  unlock  - used to unlock locked files and directories (syntax: unlock <filename>)")
    print("  read    - used to read the contents of a file (syntax: read <filename>)")
    print("  extract - used to extract the goal of a level (syntax: extract <filename>)")
    print("  quit    - ends the game")

def run():
    global current_directory
    global level_completed

    level_completed = False
    clear_screen()

    while True:
        current_directory = file_system[current_directory_path]

        command = input(str(current_directory_path) + " - $ ").strip()

        if command == "cls":
            clear_screen()

        elif command == "ls":
            list_contents()

        elif command.startswith("cd"):
            split_command = command.split(" ")
            if len(split_command) <= 1:
                print("Invalid syntax. Use 'help' to view correct syntaxes.")

            else:
                change_directory(split_command[1])

        elif command.startswith("unlock"):
            split_command = command.split(" ")
            if len(split_command) <= 1:
                print("Invalid syntax. Use 'help' to view correct syntaxes.")

            else:
                try:
                    file_system[current_directory_path + "/" + split_command[1]].unlock()

                except:
                    print("That is not a valid file or directory.")

        elif command.startswith("read"):
            split_command = command.split(" ")
            if len(split_command) <= 1:
                print("Invalid syntax. Use 'help' to view correct syntaxes.")

            else:
                read_file(split_command[1])

        elif command.startswith("extract"):
            split_command = command.split(" ")
            if len(split_command) <= 1:
                print("Invalid syntax. Use 'help' to view correct syntaxes.")

            else:
                extract_file(split_command[1])

        elif command == "quit":
            check_completion()

        elif command == "help":
            show_command_list()

        else:
            print("Command not found. Use 'help' for a list of available commands.")

        print()

        if level_completed:
            return

def tutorial():
    pass

def random_mode():
    while True:
        clear_screen()
        generate_filesystem()
        print("Level, start!")
        wait_for_input()


def generate_filesystem():
    global file_system
    print("Generating file system...")

    file_system = {}
    file_system["/home"] = Directory("home", False)

    for i in range(random.randint(0, 3)):
        file_name = "".join([random.choice(characters) for i in range(random.randint(2, 8))])
        file_system["/home/" + file_name] = Directory(file_name, False)
    print(file_system)

current_directory = None
level_completed = False
characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",\
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",\
              "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_"]
file_system = {}

main_menu()

# Test level
# file_system = {}
# file_system["/home"] = Directory("home", False)
# file_system["/home/test_1"] = Directory("test_1", True, "1234")
# file_system["/home"].contents.append(file_system["/home/test_1"])
# file_system["/home/test_1/password.txt"] = File("password.txt", "The password for test_2 is: 'p.><*as?swor/d'", False)
# file_system["/home/test_1"].contents.append(file_system["/home/test_1/password.txt"])
# file_system["/home/test_1/test_2"] = Directory("test_2", True, "p.><*as?swor/d")
# file_system["/home/test_1"].contents.append(file_system["/home/test_1/test_2"])
# file_system["/home/test_1/test_2/level_1.goal"] = Goal("level_1.goal", "Don't extract me? pls")
# file_system["/home/test_1/test_2"].contents.append(file_system["/home/test_1/test_2/level_1.goal"])
# current_directory_path = "/home"
# run()
# check_completion()

# Level 1
clear_screen()
print("Hi there! Welcome to HACK. This is PeanutButterGames' first game. Hopefully you enjoy it!")
print("Anyways, I'm _peanutButter. I'm going to give you a brief rundown of how things work in HACK.")
print("You could probably call this a tutorial.")
print()
print("HACK is presented as a very minimalistic terminal. In fact, it runs directly in your")
print("computer's terminal emulator, err, command prompt. Authentic, huh?")
wait_for_input()
clear_screen()
print("HACK's 'story mode' is very simple. Your goal is to hunt down files ending with the")
print("'.goal' extension scattered throughout a number of fabricated file systems. I didn't explain")
print("that very well, but you'll understand soon enough.")
print()
print("In case you've never used a terminal before, let me explain what they're used for and how")
print("they're used. Terminals use simple commands that, when used in tandem with other, similar")
print("commands, let you carry out some pretty complex actions. Almost everything you can do with")
print("your computer's graphical user interface can be done using its terminal emulator.")
wait_for_input()
clear_screen()
print("There are 8 different commands that you can use in your HACK terminal. The next 'slide'")
print("will explain each one's function.")
wait_for_input()
clear_screen()
show_command_list()
wait_for_input()
clear_screen()
print("Please note that the list shown in the last 'slide' can be viewed at any time using the")
print("'help' command.")
wait_for_input()
clear_screen()
print("Now that that's out of the way, I'll start up the game for you. Please enjoy!")
wait_for_input()
clear_screen()
print("Level 1")
wait_for_input()

file_system = {}
file_system["/home"] = Directory("home", False)

file_system["/home/level_1.goal"] = Goal("level_1.goal", "Whoo hoo, you can read!")
file_system["/home"].contents.append(file_system["/home/level_1.goal"])

current_directory_path = "/home"
run()
check_completion()

# Level 2
clear_screen()
print("Well done! If you're reading this, that means you've completed the first level.")
print("That tells me that you're understanding the gist of the game.")
wait_for_input()
clear_screen()
print("Level 2")
wait_for_input()

file_system = {}
file_system["/home"] = Directory("home", False)

file_system["/home/desktop"] = Directory("desktop", False)
file_system["/home"].contents.append(file_system["/home/desktop"])

file_system["/home/desktop/level_2.goal"] = Goal("level_2.goal", "Almost to the end of level 2!")
file_system["/home/desktop"].contents.append(file_system["/home/desktop/level_2.goal"])

current_directory_path = "/home"
run()
check_completion()

# Level 3
clear_screen()
print("Nice! Things are going to start getting harder now. Get ready! Don't forget that")
print("you can read the contents of a file with the 'read' command.")
wait_for_input()
clear_screen()
print("Level 3")
wait_for_input()

file_system = {}
file_system["/home"] = Directory("home", False)

file_system["/home/desktop"] = Directory("desktop", False)
file_system["/home"].contents.append(file_system["/home/desktop"])

file_system["/home/desktop/stuff"] = Directory("stuff", True, "1234")
file_system["/home/desktop"].contents.append(file_system["/home/desktop/stuff"])

file_system["/home/desktop/password.txt"] = File("password.txt", "stuff's password is: '1234'.", False)
file_system["/home/desktop"].contents.append(file_system["/home/desktop/password.txt"])

file_system["/home/desktop/stuff/level_3.goal"] = Goal("level_3.goal", "Final stretch!")
file_system["/home/desktop/stuff"].contents.append(file_system["/home/desktop/stuff/level_3.goal"])
current_directory_path = "/home"
run()
check_completion()

# Level 4
clear_screen()
print("Level 4")
wait_for_input()

file_system = {}
file_system["/home"] = Directory("home", False)

file_system["/home/desktop"] = Directory("desktop", False)
file_system["/home"].contents.append(file_system["/home/desktop"])

file_system["/home/desktop/passchars"] = Directory("passchars", False)
file_system["/home/desktop"].contents.append(file_system["/home/desktop/passchars"])

file_system["/home/desktop/passchars/1"] = Directory("1", False)
file_system["/home/desktop/passchars"].contents.append(file_system["/home/desktop/passchars/1"])

file_system["/home/desktop/passchars/1/passchar.txt"] = File("passchar.txt", "4", False)
file_system["/home/desktop/passchars/1"].contents.append(file_system["/home/desktop/passchars/1/passchar.txt"])

file_system["/home/desktop/passchars/1/3"] = Directory("3", False)
file_system["/home/desktop/passchars/1"].contents.append(file_system["/home/desktop/passchars/1/3"])

file_system["/home/desktop/passchars/1/5"] = Directory("5", False)
file_system["/home/desktop/passchars/1"].contents.append(file_system["/home/desktop/passchars/1/5"])

file_system["/home/desktop/passchars/1/3/passchar.txt"] = File("passchar.txt", "8", False)
file_system["/home/desktop/passchars/1/3"].contents.append(file_system["/home/desktop/passchars/1/3/passchar.txt"])

file_system["/home/desktop/passchars/1/5/passchar.txt"] = File("passchar.txt", "9", False)
file_system["/home/desktop/passchars/1/5"].contents.append(file_system["/home/desktop/passchars/1/5/passchar.txt"])

file_system["/home/desktop/passchars/2"] = Directory("2", False)
file_system["/home/desktop/passchars"].contents.append(file_system["/home/desktop/passchars/2"])

file_system["/home/desktop/passchars/2/passchar.txt"] = File("passchar.txt", "3", False)
file_system["/home/desktop/passchars/2"].contents.append(file_system["/home/desktop/passchars/2/passchar.txt"])

file_system["/home/desktop/passchars/2/4"] = Directory("4", False)
file_system["/home/desktop/passchars/2"].contents.append(file_system["/home/desktop/passchars/2/4"])

file_system["/home/desktop/passchars/2/6"] = Directory("6", False)
file_system["/home/desktop/passchars/2"].contents.append(file_system["/home/desktop/passchars/2/6"])

file_system["/home/desktop/passchars/2/4/passchar.txt"] = File("passchar.txt", "1", False)
file_system["/home/desktop/passchars/2/4"].contents.append(file_system["/home/desktop/passchars/2/4/passchar.txt"])

file_system["/home/desktop/passchars/2/6/passchar.txt"] = File("passchar.txt", "0", False)
file_system["/home/desktop/passchars/2/6"].contents.append(file_system["/home/desktop/passchars/2/6/passchar.txt"])

file_system["/home/desktop/password.txt"] = File("password.txt", "stuff's password is 912688.", True, "438190")
file_system["/home/desktop"].contents.append(file_system["/home/desktop/password.txt"])

file_system["/home/desktop/stuff"] = Directory("stuff", True, "912688")
file_system["/home/desktop"].contents.append(file_system["/home/desktop/stuff"])

file_system["/home/desktop/stuff/level_4.goal"] = Goal("level_4.goal", "Yay, level 4 complete!")
file_system["/home/desktop/stuff"].contents.append(file_system["/home/desktop/stuff/level_4.goal"])

current_directory_path = "/home"
run()
check_completion()

# Finish
clear_screen()
print("Congrats! You've made it to the end of the 'story' mode as it is right")
print("now. Hopefully you enjoyed it!")
print()
print("Also, I plan on working on this a bunch more in the future, and hopefully")
print("crank out a full length story mode I can be proud of with a ton of different")
print("and unique 'hacker'-esque mechanics.")
print()
print("Don't forget to check back in later if you're interested in seeing the")
print("improvements I make and puzzles/mechanics I add!")
wait_for_input()
clear_screen()
