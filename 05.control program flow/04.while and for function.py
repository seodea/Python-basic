# While, for function (Loop Statement)

# This 'While function' will help you if you want to make a loop program until data is True.

print('How many time do you want to repeat it? : ')
limit = int(input())

count = 0
while count < limit :
    count = count + 1
    print('{0} time repeat.'.format(count))

print('End')

# Also you can use the 'If function' in 'while function'
# And you can make a 'Infinite Loop' by 'while function'

while True:
    print('Do you want to reapeat? [Yes/No]')
    answer = input()

    if answer == 'Yes' :
        print('Repeat')

    elif answer == 'No' :
        print('Stop to repeat')
        break

    else :
        print('It is wrong answer')

# This 'for method' is little bit different.
# 'For method' is repeated using sequence like 'list', 'tuple', 'string'.

for i in (1, 2, 3):
    pring(i)

# That sequence is three tuple. So That for program can repeat three.

for list in ['Hello', 'Python', 'Programer'] :
    print(list)

for string in 'Hello Python Programer' :
    print(string)

# But Many programer use the 'range' for sequence in for program.

for i in range(0,5,1) :
    print(i)

# The 0 number means start value.
# The 5 number means stop value.
# The 1 number means increasing value.

for i in range(0,5):
    print(i)

# The increasing value is not necessary.

for i in range(5):
    print(i)

# Also the start value is not necessary.

# For example, you can make a program of add the number 1 to 10.

a = 0
for i in range(1,10):
    a = a + i
    print(a)


    
