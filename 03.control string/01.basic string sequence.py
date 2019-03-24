# You can use the ' ', if you want to use the string.
a = 'Hello Python'
a

# You can use the " ", if you want to use the string.
b = "Hello Python"
b

# You can use the """ """, if you want to use the string in other line.
c = """Welcom to
Python"""
c

# You can check the value. class str means your value is string.
type(c)


# You can control the string useing the sequence.
hello = 'Hello'
python = 'Python'

hello_python = hello + '_' + python
hello_python

# [0:5] means you can export only string from 0 to before 5.
d = 'Hello Python'
d[0:5]

# Also you can change the number.
d[0:5]
d[6:12]

# And this sequence is same to before([0:5]).
d[:5]

# This sequence can be export from 6 to end.
d[6:]

# This sequence can be export unique letter.
d[0]
d[6]

# This 'in' sequence is mean you can check the unique letter in string.
# for example, if 'hello' word is in 'd' value, this command is 'Ture'
'Hello' in d # this command is Ture
'hello' in d # this command is False

# If you want to check string length, you can use the len() command in python.
len(d)

