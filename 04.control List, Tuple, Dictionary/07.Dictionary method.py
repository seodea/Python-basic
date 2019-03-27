# We can control the dictionary to use the dictionary method if you want.

# keys()
# We can check the keys in the dictionary.

dic = {}
dic['Python'] = 'www.python.org'
dic['Microsoft'] = 'www.microsoft.com'
dic['Apple'] = 'www.apple.com'

dic.keys()
'Python' in dic.keys()
'Goggle' in dic.keys()

# items()
# We can check the key and values in the dictionary.

dic.items()
'www.python.org' in dic.items()
'www.google.com' in dic.items()

# values()
# We can check the values in the dictionary.

dic.values()
'www.python.org' in dic.values()
'www.google.com' in dic.values()

# pop()
# We can remove the key and value in the dictionary.

dic.pop('Apple')
dic

# clear()
# We can do reset the dictionary.

dic.clear()
dic



