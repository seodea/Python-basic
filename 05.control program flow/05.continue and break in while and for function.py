# continue and break method

# You can controll the your 'while' and 'for' method to use the 'continue' or 'break'.

# Next program is example for contiune.

for i in range(10) :
    if i % 2 == 1 :
        continue

    print(i)

# Next program is example for break.

i = 0
while True :
    i = i+1
    if i == 100 :
        print('i is {0}. stop the program.'.format(i))
        break

    print(i)


# Also you can use the continue and break in one program.

print('How many time do you want to repeat? (1 to 20) : ')
repeat = int(input())
for i in range(1,20) :   

    if i == repeat :
        print('Stop to repeat until {0}.'.format(repeat))
        break

    elif i % 2 == 1 :
        continue
    print(i)

