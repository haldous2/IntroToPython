
## Playing around with files

# Create new file
#
# Modes:
# 'r'     open for reading (default)
# 'w'     open for writing, truncating the file first
# 'x'     open for exclusive creation, failing if the file already exists
# 'a'     open for writing, appending to the end of the file if it exists

# 'b'     binary mode
# 't'     text mode (default)
# '+'     open a disk file for updating (reading and writing)
# 'U'     universal newlines mode (deprecated)

# Text file
with open('files_lab.txt', 'wt') as f:
    for x in range(0,100):
        f.write("line: %i\n" % x)

# Binary file
# I can open this in a text editor, what's the diff between a text file ?
with open('files_lab_bin.txt', 'wb') as f:
    for x in range(0,100):
        f.write("line: %i\n" % x)

# Open and write out text file
with open('files_lab.txt', 'r') as f:
    for x in f:
        print x

