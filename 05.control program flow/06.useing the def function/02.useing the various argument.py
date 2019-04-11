# You can use the various argument in 'def function'
# You can set a 'default argument value' and 'keyword argument'.

# default argument value

def print_string(text, count=1):
    for i in range(count):
        print(text)

print_string('hello')
print_string('hello', 4)

# keyword argument value

def print_personnel(name, position='staff', nationality='Korea'):
    print('name = {0}'.format(name))
    print('position = {0}'.format(position))
    print('nationality = {0}'.format(nationality))

print_personnel('Dominic')
print_personnel('Dominic', 'owner')
print_personnel('Dominic', 'owner', 'USA')
print_personnel('Dominic', nationality = 'UK')
print_personnel('Dominic', position = 'owner')

# arbitrary argument list

def merge_string(*text_list):
    result = ''
    for s in text_list:
        result = result + s
    return result

merge_string('You', 'are', 'useing', 'the', 'python')

# This text_list argument is the Tuple.
# If you use the *, it is the tuple.
# If you use the **, it is the dictionary.

def print_team(**players):
    for k in players.keys():
        print('{0} = {1}'.format(k, players[k]))

print_team(Messi = 'FW', Son = 'FW', Pepe = 'DF', Casillas = 'GK')

# But the default argument value befor the arbitrary argument can't use the keyword argument.

def print_args(argc, *argv):
    for i in range(argc):
        print(argv[i])

print_args(3, 'argv1', 'argv2', 'argv3')

# It's running
# But If you use the keyword argument instead of default argument, It won't run.

print_args(argc=3, 'argv1', 'argv2', 'argv3')

# But On the contrary, you have to use the keyword argument instead of default argument.

def print_args(*argv, argc):
    for i in range(argc):
        print(argv[i])

print_args('argv1', 'argv2', 'argv3', argc=3)

# It's running

print_args('argv1', 'argv2', 'argv3', 3)

# But It isn't running



