# Local variable and Global variable

# You should to know how to use the variable in loacal or gloabal.

def scope_test():
    a = 1
    print('a:{0}'.format(a))

a = 0

# Do you think if i call 'a' variable after useing the def of scope_test, what is a number?
# 0 or 1? 

scope_test()

print('a:{0}'.format(a))

# This answer is 0.
# Because the a variable in def of scope_test is one thing, a variable outside def of scope_test is another.
# But If you want to use the variable in def, you can use the global for changing from local variable to global variable.

def scope_test():
    global a
    a = 1
    print('a:{0}'.format(a))

a = 0

scope_test()

print('a:{0}'.format(a))

# This answer is 1.
# Also you can use the return function.

def scope_test():
    a = 1
    print('a:{0}'.format(a))
    return a

a = 0

a = scope_test()

print('a:{0}'.format(a))

# This answer is 1 as well.
