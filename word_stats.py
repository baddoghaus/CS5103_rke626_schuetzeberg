import sys # lib used for cmd line args

word_dict = {} # declair dictory of words:occurences
lineCount = 0  # declair a variable to hold the number of lines
characterCount = 0 #declair a varialbe to hold the number of characters

#print("The input file has the name %s" % (sys.argv[1])) 
#print("The output file has the name %s" % (sys.argv[2]))

# count the number of lines in argv[1]
lineCount = len(open(sys.argv[1]).readlines())

# count the number of characters in a file
characterCount = len(open(sys.argv[1]).read())

# open argv[1] as input file object -strip of '\n' -split text at spaces
with open(sys.argv[1], "r") as input_doc:
    word_list = [line.rstrip('\n').split(' ') for line in input_doc]

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

# clean up memory
input_doc.close()
output_doc.close()

