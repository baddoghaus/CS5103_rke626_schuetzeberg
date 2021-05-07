"""Word Processor"""

import sys # lib used for cmd line args
import os # lib used to delete files
from subprocess import check_output # lib used to perfrom mock test

word_dict = {} # declair dictory of words:occurences
input_file = sys.argv[1] # set input_file variable as the input file
out_file = open("out_file.txt", "w") # set outputFile varialbe as the output file

def line_counter(input_file):
    """define function "line_counter" to count the number of lines in a file"""
    if type(input_file) not in [str]:
        print("The input_file parameter passed to line_counter() is not of type str")
        raise TypeError
    try:
        with open(input_file, "r") as in_file:
            length = len(in_file.readlines())
    except FileNotFoundError:
        print("The input_file passed to line_counter() does not exist")
        raise
    else:
        return length

def character_counter(input_file):
    """define function "character_counter" to count the number of character in a file"""
    if type(input_file) not in [str]:
        print("The input_file parameter passed to character_counter() is not of type str")
        raise TypeError
    try:
        with open(input_file, "r") as in_file:
            length = len(in_file.read())
    except FileNotFoundError:
        print("The input_file passed to character_counter() does not exist")
        raise
    else:
        return length

def word_counter(input_file):
    """define function "word_counter" to count the frequency of each unique word in a file"""
    if type(input_file) not in [str]:
        print("The input_file parameter passed to word_counter() is not of type str")
        raise TypeError
    try:
        with open(input_file, "r") as in_file:
            # store contents of file to word_list -strip of '\n' -split text at spaces
            word_list = [line.rstrip('\n').split(' ') for line in in_file]
        # flatten nested list
        word_list = [item for sublist in word_list for item in sublist]
        # generate (words:occurence) dictionary from word_list
        word_dict.clear()
        for word in word_list:
            word_dict[word] = word_dict.get(word, 0) + 1
    except FileNotFoundError:
        print("The input_file passed to word_counter() does not exist")
        raise
    else:
        return word_dict


def word_replacer(input_file):
    """define function "word_replacer" to replace occurances
    of a given pattern with a given replacement pattern"""
    if type(input_file) not in [str]:
        print("The input_file parameter passed to word_replacer() is not of type str")
        raise TypeError
    try:
        #old_word = get_input("Please enter pattern to be replaced:\n");
        #new_word = get_input("Please enter replacement pattern:\n");
        # open intermediate file to store txt after word replacements
        with open("intermediate.txt", "w+") as intermediate:
            with open(input_file, "r") as in_file:
                for line in in_file:
                    old_word = get_input("Please enter pattern to be replaced:\n")
                    new_word = get_input("Please enter replacement pattern:\n")
                    intermediate.write(line.replace(str(old_word), str(new_word)))
                intermediate.seek(0)
            in_file.close()
            with open(input_file, "w") as in_file:
                for line in intermediate:
                    in_file.write(line)
                    written_line = line.rstrip('\n')
            os.remove("intermediate.txt")
    except FileNotFoundError:
        print("The input_file passed to word_replacer() is not of type str")
        raise
    else:
        return written_line

def dict_print(word_dict):
    """define function "dict_print" to print word dictionary of working file in ABC order"""
    for key, value in sorted(word_dict.items()):
        print(key, value)

def dict_write(word_dict, out_file):
    """define function "dict_write" to write word dictionary in ABC order"""
    for key, value in sorted(word_dict.items()):
        out_file.write('{} {}\n'.format(key, value))

def line_print(lines):
    """define function "line_print" to print the number of lines in working file"""
    print("\nThere are " + str(lines) + " lines in the input file.")

def line_write(lines, out_file):
    """define function "line_write" to write the number of lines in working file"""
    out_file.write("\nThere are {} lines in the input file.\n".format(lines))

def character_print(characters):
    """define function "character_print" to print the number of characters in working file"""
    print("\nThere are {} characters in the input file.".format(characters))

def character_write(characters, out_file):
    """define function "character_write" to write the number of characters in working file"""
    out_file.write("\nThere are {} characters in the input file.\n".format(characters))

def get_input(text):
    """define function "get_input" to process user input"""
    return input(text)

# perform an initial analysis of input file
word_counter(input_file)
line_count = line_counter(input_file)
character_count = character_counter(input_file)
dict_print(word_dict)
line_print(line_count)
character_print(character_count)

# define file interaction
ACTION = 0
while ACTION != 5:
    # print interaction menu
    print("Menu\n")
    print("1: Replace a word\n")
    print("2: Print word dictionary of working file in ABC order\n")
    print("3: Print the number of lines in working file\n")
    print("4: Print the number of characters in working file\n")
    print("5: Exit file interaction and write results to out_file.txt\n")
    ACTION = int(input("Please input your desired ACTION.\n"))

    # define interaction logic
    if ACTION == 1:
        word_replacer(input_file)
        word_counter(input_file)
        line_count = line_counter(input_file)
        character_count = character_counter(input_file)
    elif ACTION == 2:
        dict_print(word_dict)
    elif ACTION == 3:
        line_print(line_count)
    elif ACTION == 4:
        character_print(character_count)
    else:
        continue

# write final file form to out_file
dict_write(word_dict, out_file)
line_write(line_count, out_file)
character_write(character_count, out_file)

# close out_file (with block's close in_file)
out_file.close()
