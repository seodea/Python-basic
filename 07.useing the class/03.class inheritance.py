# class inheritance

# You can do the inheritance as data attribute or method from the base class to the deroved class.

class Base:
    def base_method(self):
        print("base_method")

class Derived(Base):
        pass

base = Base()
base.base_method()

# You can see the 'base_method'.
# Now we can call the derived class.

dervied = Derived()
dervied.base_method()

# Do you know what it is different?
# Yes. You can call the base_metheod funtion in Derived class.

# Now we can check the data attribute of base class.

class A:
    def __init__(self):
        print('A.__init__()')
        self.message = 'Made In A'

class B:
    def __init__(self):
        print('B.__init__()')

obj = B()
obj.message

# We can't see the error that we can't call the message method.
# Do you know Why we can't use the message?

# The Python program want to call directly method anything.

class A:
    def __init__(self):
        print('A.__init__()')
        self.message = 'Made In A'

class B:
    def __init__(self):
        A.__init__(self) # I add the line for calling the A method.
        print('B.__init__()')

obj = B()
obj.message

# Finally, We can see the class A message.

# If We want to use the another class method as like changing the class name (class B(A) -> class B(Z)), We should change the all of code in class B line.
# It means we should change the code from A.__init__(self) to Z.__init__(self) in class B.
# Do you want to change the all of code?
# That isn't easy if you have long line in your program.

# So the Python help you to use the 'super()' function.

# 3.1 super()
class A:
    def __init__(self):
        print('A.__init__()')
        self.message = 'Made In A'

class B(A):
    def __init__(self):
        print('B.__init__()')

        super().__init__() # This is same the result as like A.__init__
        print('self.message is' + self.message)

if __name__ == '__main__':
    b = B()

# You can see the coed running well.

class Base:
    def __init__(self):
        print("Base")

class Derived(Base):
    pass

d = Derived()

# If the Derived have only a pass code, It call the Base __init__() method.

# 3.2 multiple inheritance
# Python can support to get many class method.

class A:
    pass

class B:
    pass

class C:
    pass

class D(A,B,C):
    pass

# It has very important things when you use the multiple inheriitance.

class A:
    def method(self):
        print('A')

class B(A):
    def method(self):
        print('B')

class C(A):
    def method(self):
        print('C')

class D(B,C):
    pass

obj = D()
obj.method()

# You can see the anwser 'B'.
# Python should use the first class method when it use the multiple inheritance.

# 3.3 overriding

class A:
    def method(self):
        print('A')

class B(A):
    def method(self):
        print('B')

class C(A):
    def method(self):
        print('C')

A().method()

B().method()

C().method()

# you can use the same method in each other class.
