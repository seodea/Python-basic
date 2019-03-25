# This command is string method

# Startswith()
# This command can verify that the original string starts with a parameter.
# The result is the 'True' or 'False'
a = 'Hello'
a.startswith('He')
a.startswith('he')

# endswith()
# This command can verify that the original string ends with a parameter.
# The result is the 'True' or 'False'
a = 'Hello'
a.endswith('He')
a.endswith('lo')

# find()
# This command can verify the parameter in original string from starting.
# The result is the 'True' or 'False'.
# But the result is the '-1, if the parameter isn't in original string. 
a = 'Hello'
a.find('ll')
a.find('He')
a.find('Py')

# rfind()
# This command can verify the parameter in original string from end.
# The result is the 'True' or 'False'.
# But the result is the '-1, if the parameter isn't in original string. 
a = 'Hello'
a.rfind('H')
a.rfind('lo')
a.rfind('W')

# count()
# This command can count the parameter in original string.
# The result is the nnumber.
a = 'Hello'
a.count('l')

# lstrip()
# This command remove the blank in origianl string from left.
'      Left Strip'.lstrip()

# rstrip()
# This command remove the blank in origianl string from right.
'Right Strip      '.rstrip()

# strip()
# This command remove the blank in origianl string both left and right.
'      Strip      '.strip()

# isalpha()
# This command remove the blank in origianl string from left.
# The result is the 'True' or 'False'.
'ABCDefgh'.isalpha()
'123ABC'.isalpha()

# isnumeric()
# The result is the 'True' or 'False'.
'1234'.isnumeric()
'123ABC'.isnumeric()

# isalunm()
# The result is the 'True' or 'False'.
'123ABC'.isalnum()
'1234'.isalnum()
'ABC'.isalnum()
'1234 ABC'.isalnum()

# replace()
a = 'Hello, Pyhon'
b = a.replace('Python', 'World')
a
b

# split()
# This command can split the original string from parameter and making the list. after split.
a = 'Apple, Orange, Mango'
b = a.split(',')
b
type(b)

a = 'Split'
b = a.split('l')
b
type(b)

# upper()
# This command can change the alphabet from lower alphabet to upper alphabet.
a = 'lower case'
b = a.upper()
a
b

# lower()
# This command is the opposite of 'upper()' command.
a = 'UPPER CCASS'
b = a.lower()
a
b

# format()
# This command can make formatted string that you want to make string.
a = 'My name is {0}. I am {1} years old.'.format('Seodea', 30)
a
b = 'My name is {name}. I am {age} years old'.format(name='Seodea', age=30)
b





