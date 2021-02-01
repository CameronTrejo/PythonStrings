#Python Strings

# Python is loosely typed -- data types

# String variableName -- Java C++ Swift OBJ Oriented Languages
# String variableName = "This is a string"
# Int variableInt = 34 --> Integer

# Python 
# variableName = "This is a sring" ---> String
# variableName = 3 ---> String
# variableInt = 34 --> Integer


# Python is a scripting language
# -- Python can run on anything that alows the interpreter to be installed
# -- Does not require compile
# -- You won't know failure of the code until you run it.
# -- Slower to ru through the interpreter

# String is a list of characters
#      Character [a-z,A-Z,]
#      Number [0-9]
#      Special Character [@#$%^]
#      Space [ ]
#      Escape Character [\n --> newline, \t --> tab, \\]

School = 'WEBER STATE'

print ('first character is:', School[0])
print ('Second character is:', School[1])

print ('Last character is:', School[-1])
print ('Second to last character is:', School[-2])

first_name = 'Cameron' # -- String data type
last_name = 'Trejo' # -- String data type

initials = 'Initials:', first_name[0], last_name[0]

first_initial = first_name[0]
last_initial = last_name[0]

print(initials)
print('Initials:', first_initial, last_initial)
print('Initials:', first_initial + last_initial)


first_three_first_name = first_name[0:3]

print(first_three_first_name)

capital_name = first_name.upper()
print(capital_name)








