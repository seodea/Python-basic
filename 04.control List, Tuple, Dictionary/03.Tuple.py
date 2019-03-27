# Frist Tuple can support to change or remove the data. (but list is possible)
# The tuple is the immutable type.
# You should use the '(' and ')' if you want to make a 'Tuple'.

a = (1, 2, 3)
a
type(a)

# You can make the 'Tuple' without '(' and ')'
a = 1, 2, 3, 4
a
type(a)

b = 'a', 'b', 'c'
b
type(b)

# If we want to use the only one data for Tuple, we use the another way.

a = (1)
a
type(a)

# We should use the ',' if we want to make Tuple with only one data.
a = (1,)
a
type(a)

b = 1,
b
type(b)

# The Tuple is possible the control command such as list.

# slicing
a = (1, 2, 3, 4, 5)
a[:3]
a[4:6]

# +
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
a
b
c

# Find data to use the location
a = (1, 2, 3)
a[1]
a[1] = 5 # It isn't possible in tuple

# len()
a = (1, 2, 3)
len(a)






