# Decoration method in class

# Someone maybe want to use the class without self as like just easier or want to call the class itself.
# I think if you use the Decoration method, It help you.


# @statcimethod
# @staticmethod isn't necessary self parametar.

class static:
    @staticmethod
    def plus(a,b):
        return a+b

obj = static()
obj.plus(3, 5)
a = static.plus(3, 5)

class Calculator:

    @staticmethod
    def plus(a, b):
        return a+b
    
    @staticmethod
    def minus(a, b):
        return a-b

    @staticmethod
    def multiply(a, b):
        return a*b

    @staticmethod
    def divide(a, b):
        return a/b

if __name__ == '__main__':
    print('{0} + {1} = {2}'.format(7, 4, Calulator.plus(7, 4))) # @staticmethod is possible to call class.method() without the instance name.
    print('{0} + {1} = {2}'.format(7, 4, Calulator.minus(7, 4)))
    print('{0} + {1} = {2}'.format(7, 4, Calulator.multiply(7, 4)))
    print('{0} + {1} = {2}'.format(7, 4, Calulator.divide(7, 4)))
    
# @classmethod
# @classmethod should use the cls instead of self.

class TestClass:
    @classmethod
    def print_TestClass(cls):
        print(cls)

TestClass.print_TestClass() # Classmethod is called by class
obj = TestClass()
obj.print_TestClass() # Classmethod is called by instance

# Yes. The classmethod call class.
# I make a easier code to use classmethod.

class InstanceCounter:
    count = 0

    def __init__(self):
        InstanceCounter.count += 1

    @classmethod
    def print_instance_count(cls):
        print(cls.count)

if __name__ == '__main__':
    a = InstanceCounter()
    InstanceCounter.print_instance_count()

    b = InstanceCounter()
    InstanceCounter.print_instance_count()

    c = InstanceCounter()
    c.print_instance_count()

# You know what this class count is raise automatically when you call the class.

# __call__ and @
# __call__ method is the magic method that you can use the object for calling the other funtion.

class MyDecorator:
    def __init__(self, f):
        print('Initializing Mydecorator...')
        self.func = f 

    def __call__(self):
        print('Begin :{0}'.format(self.func.__name__))
        self.func()
        print('End :{0}'.format(self.func.__name__))


def print_hello():
    print('Hello.')

print_hello = MyDecorator(print_hello) # print_hello isn't the function over the code. It's a object in Medecorator.

print_hello()


# Also you can use the @ instead of __call__.
# This code is more easier than __call__ code.

class MyDecorator:
    def __init__(self, f):
        print('Initializing Mydecorator...')
        self.func = f

    def __call__(self):
        print('Begin :{0}'.format(self.func.__name__))
        self.func()
        print('End :{0}'.format(self.func.__name__))


@MyDecorator
def print_hello():
    print('Hello.')

