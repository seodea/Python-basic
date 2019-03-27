# We can control the list to use the list method if you want.

# append()
# add the date on last.
a = [1,2,3]
a.append(4)
a

# extend()
# this list method is same +. it add the other list.

a = [1,2,3]
a.extend([4,5,6])
a

# insert()
# We can add the date in uniqu location in list.

a = [2,3,5]
a.insert(0,1)
a
a.insert(3,4)
a

# remove()
# We cna remove the data in list.

a = ['Korea', 'Japan', 'China', 'Canada']
a.remove('Canada')
a

# pop()
# We can remove the last data in list if you use the only pop()
# Also we can remove the uniqu data in list like remove() if you put on the location number like pop(2).

a = [1,2,3,10,4,5]
a.pop()
a
a.pop(3)
a

# index()
# We can find location numver from the parameter in first data in list.

a = ['abc', 'def', 'ghi']
a.index('def')
a.index('jkl')

# count()
# We can check how many data you have in lise, such as parameter.

a = [1, 100, 2, 100, 3, 100]
a.count(100)
a.count(200)

# sort()
# We can chagne the order in ascending order if you don't use the any parameter
# But We can chang the order in descending order if you use the 'reverse = Ture' with paratemer

a = [3, 4, 1, 2, 5]
a.sort()
a
a.sort(reverse = True)
a

# reverse()
# We can reverse the order of the data in the list.

a = [3, 4, 5, 1, 2]
a.reverse()
a
b =['h', 'e', 'l', 'l', 'o']
b.reverse()


