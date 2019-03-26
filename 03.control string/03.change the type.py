# IF you use the input() command, This type is strings
# So you can't directly use the * command after useing the input() command.
a = input()
type(a)

b = input()

result = a * b

# We need to change the type sometime.
# This constructor that change the type are int(), float(), complex(), str().

int('1234567')
float('123.456')
complex('1+2j')


# You can do x command from value with string type, if you use the that constructor.
# For example, this command change the type from 'string' to 'int'.
print("write the first number : ")
a = input()
print("write the second number : ")
b = input()

result = int(a) * int(b)

print ("{0} * {1} = {2}".format(a, b, result))

# For example, this command change the type from 'int' to 'string'.
import math
type(math.pi)

text = "pi is" + str(math.pi)
text
