# def function.
# You can make a clean program if you can use the 'def function'.

# For example, I make a easy program.
# If i write the positive number, It'll pass the program.
# But if i write the negative number, It'll change the number to positive.

arg = int(input('Can you write the number for test? : '))

if ( arg < 0 ) :
    result = arg * -1
    
else :
    result = arg
    
print(result)

# But If you can use the 'def function', your program will be cleaned.

def num_check(arg):
    if ( arg < 0 ) :
        result = arg * -1
    
    else :
        result = arg

    return result


num_check(20)
num_check(-16)

# If you run the 'def function' one time, you can always call the 'def function' when you want.
# You don't need to rewrite same code in same program.

# Also You can use the many argument value in 'def function'.

def print_name(first_name, last_name):
    print('My name is {0} {1}.'.format(first_name, last_name))

print_name(smith, dominic)
