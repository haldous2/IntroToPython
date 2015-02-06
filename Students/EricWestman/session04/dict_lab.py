
## Part 1

# Create dictionary
my_dict = {"name":"Chris","city":"Seattle","cake":"Chocolate"}

print my_dict

# Remove key 'cake'
#del(my_dict["cake"])
del my_dict["cake"]

print my_dict

# Add key 'fruit'
my_dict.setdefault("fruit", "Mango")

print my_dict

# Display Keys
print my_dict.keys()

# Display Values
print my_dict.values()

# Is 'cake' a key ?
print "cake" in my_dict.keys()
print "city" in my_dict.keys()

# Is 'mango' a value ?
print "Mango" in my_dict.values()

## Part 2

# "Using the dict constructor and zip, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine)."

my_dict_numbers = dict( zip([str(i) for i in range(1, 15)],[int(i) for i in range(1, 15)]) )

print my_dict_numbers

# Using my_dict_numbers, place t's in place of numbers
for i, v in my_dict_numbers.items():
    my_dict_numbers[i] = "t" * v

print my_dict_numbers

# Sets s2,s3,s4 - 1 to 20

s2 = set(range(1,21,2))
s3 = set(range(1,21,3))
s4 = set(range(1,21,4))

print s2
print s3
print s4

# is s3 a subset of s2

print s3.issubset(s2)

# is s4 a subset of s3

print s4.issubset(s2)

## Part 5

# Create set 'Python'.. mutable (mutate-able)

my_set_python = set("Python")

print my_set_python

my_set_python.add("i")

print my_set_python

# New frozeset 'marathon'.. unmutable (not mutate-able)

my_set_marathon = frozenset("marathon")

# Union of Python & marathon

print "Union:"
print my_set_python.union(my_set_marathon)
print my_set_marathon.union(my_set_python)

# Intersection of Python and marathon

print "Intersection:"
print my_set_python.intersection(my_set_marathon)
print my_set_marathon.intersection(my_set_python)
