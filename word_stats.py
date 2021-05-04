import sys # lib used for cmd line args
import os # lib used to delete files

word_dict = {} # declair dictory of words:occurences
lineCount = 0  # declair a variable to hold the number of lines
characterCount = 0 #declair a varialbe to hold the number of characters

# count the number of lines in argv[1]
lineCount = len(open(sys.argv[1]).readlines())

# count the number of characters in a file
characterCount = len(open(sys.argv[1]).read())

# open an intermediate file to store txt after word replacements
intermediate = open("intermediate.txt", "w+")

# open argv[1] as input file object 
# replace word patterns from inputFile with argv[3] with argv[4]
# save replaced text to intermediate file "intermediate.txt"
# modify intermediate file and store to word_list -strip of '\n' -split text at spaces
with open(sys.argv[1], "r") as input_doc:
    for line in input_doc:
        intermediate.write(line.replace(sys.argv[3], sys.argv[4]))
    intermediate.seek(0)
    word_list = [line.rstrip('\n').split(' ') for line in intermediate]

# flatten nested list
word_list = [item for sublist in word_list for item in sublist]

# open argv[2] as the output file object
output_doc = open(sys.argv[2], "w")

# generate (words:occurence) dictionary from word_list
for word in word_list:
    word_dict[word] = word_dict.get(word, 0) + 1

# print word_dict in abc order
for key,value in sorted(word_dict.items()):
    print(key, value)
    output_doc.write('{} {}\n'.format(key, value))

# print number of lines in doc
print("\nThere are " + str(lineCount) + " lines in the input file.")
output_doc.write("\nThere are {} lines in the input file.\n".format(lineCount))

# print number of characters in doc
print("\nThere are {} characters in the input file.".format(characterCount))
output_doc.write("\nThere are {} characters in the input file.\n".format(characterCount))

# close input, intermediate, and output file's
input_doc.close()
output_doc.close()
intermediate.close()

# delete intermediate file
os.remove("intermediate.txt")
