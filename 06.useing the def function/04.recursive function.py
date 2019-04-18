# Recursive Function.

# Recursive function means to call function my self.

def some_func(count):
    if count > 0:
        some_func(count-1)

    print(count)

# You can creat the factorial program to use recursibe function.

def factorial(n):
    if n == 0 :
        return 1
    elif n > 0 :
        return factorial(n-1)*n


# Recursive function is so confuse when you want to use this function in big program.
# I think you should understand the recursive function flow before you use this function.
