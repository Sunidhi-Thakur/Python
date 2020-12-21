#create a tuple
tup1 = ()
print(tup1)
print('\n')

#tuple with different data types
tup2 = (-1, 8.1, "Sunidhi", True )
print(tup2)
print('\n')

#create a number with tuple and print one item
tup3 = (1,3,5,6,7,8,9)
print(tup3)
print("First element is: ",tup3[0])
print('\n')


# add an item in tuple
tup4 = (9, 4, 6, 1, 4, 5, 2) 
print(tup4)
tup5 = tup4 + (0,)
print(tup5)
print('\n')

# convert a tuple to string
tup6 = ('S', 'U', 'N', 'I', 'D', 'H', 'I')
print(tup6)
print(type(tup6))
st =  ''.join(tup6)
print(st)
print(type(st))
print('\n')