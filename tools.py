# randomly re order the lines in three.txt
import random
def reorder():
    with open("assets/three.txt", "r") as f:
        lines = f.read().splitlines()
        random.shuffle(lines)
        with open("three.txt", "w") as f:
            for line in lines:
                f.write(line + "\n")

# remove blank lines
def remove_blanks():
    with open('assets/three.txt', 'r') as f:
        lines = f.readlines()
    with open('assets/three.txt', 'w') as f:
        for line in lines:
            if line.strip():
                f.write(line)

# remove all lines that have a number as the first character in working_snapchat.txt
def remove_numbers():
    with open('assets/working_snapchat.txt', 'r') as f:
        lines = f.readlines()
    with open('assets/working_snapchat.txt', 'w') as f:
        for line in lines:
            if not line[0].isdigit():
                f.write(line)