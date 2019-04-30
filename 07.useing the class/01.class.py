# class

# The class have a attribute and a method.
# If you use the class, your code will be simple.

# For example,

color = 0xFF0000
wheel_size = 16
displacement = 2000

def forward():
    pass

def backward():
    pass

def turn_left():
    pass

def turn_right():
    pass

# This example isn't class. It isn't not together.
# The class will make a only one thing.

class Car:
    def __init__(self):
        self.color = 0xFF0000
        self.wheel_size = 16
        self.displacement = 2000

    def forward(self):
        pass

    def backward(self):
        pass

    def turn_left(self):
        pass

    def turn_right(self):
        pass

# This is class data type. It is class not yet.
# We have to make a class like instance.
    
num = 123 # data type : int, variable : num
my_car = Car() # data type : Car class, object : my_car

# So, you can use the class code.

# Calling way
my_car.color
my_car.wheel_size

# Calling the information of my car
print('0x{:02X}'.format(my_car.color)) 
print(my_car.wheel_size)               
print(my_car.displacement)             

# Calling the method of my_car
my_car.forward()    
my_car.backward()   
my_car.turn_left()  
my_car.turn_right()

