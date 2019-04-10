# You can use the logical operator when you want to get the True or False result.

# bool data type
# The bool data type is the data type that tells two values of "True or False".

a = 3 > 2
a

b = 2 > 3
b

type(a)
type(b)

# logical operator
# The 'not, and, or' is the logical operator

# 'not' logical operator
not True
not False

# You can use the 'not' logical operator for number, string, tuple, list, dictionary.
# The number '0' and 'None' is False.
not 0
not None

# The other number is True.
not 1
not -1

# The string, Tuple, List, Dictionary of blank status is 'False'

not ''
not ()
not []
not {}
not 'ABC'
not (1,2,3)

# 'and' logical operator
# It is True if the two data is True.
# But it is false if only one data is True.

True and True
True and False

a = 1
b = 2
if a == 1 and b == 2:
    True
else:
    False

# 'or' logical operator
# It is True if only one data is True.

False or True
False or False

a = 1
b = 2
if a == 2 or b == 2:
    True
else:
    False



