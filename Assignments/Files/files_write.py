# Get input of a filename to read and get another input of a filename to write.
# Read the contents of the file to read and capitalize the letters and store it in the file to write.
# At the end print Done.
# Output Start
# Enter file to read:
# test1.txt
# Enter file to write:
# test1-upper.txt
# Done
# Output End
# File test1.txt has these content
# Hello World
# After running the program file test1-upper.txt has this
# HELLO WORLD

fname = input("Enter source file name: ")
try:
    fhand = open(fname, 'r')
except:
    print("File cannot be opened")
    quit()
inp = fhand.read()
uppercase = inp.upper()
addname = input("Enter 'to edit' file name : ")
appen = open(addname, 'a')
appen.write(uppercase)
capname = input("Enter new file name: ")
output = open(capname, 'w')
output.write(uppercase)
print("Done")
print('File', fname, ":")
print(inp)
print('File', capname, ":")
print(uppercase)
