# Private member

# If you want to use the class member that only use the member in class.
# It means you can't call the private member outside of class.

# The private member has a rule.

# 1. Two underscores must be prefixes. __ ex) __number
# 2. Suffixes are allowed up to one underscore. ex) __number_
# 2.1 If Suffixes are two underscore, It is public member ex) __number__ 

class HasPrivate:
    def __init__(self):
        self.public = 'Public.'
        self.__private = 'Private'

    def print_from_internal(self):
        print(self.public)
        print(self.__private)

obj = HasPrivate()
obj.print_from_internal()

print(obj.pulic)
print(obj.__private) # You can see the error code.



