#create a set
set1 = {1, 2, 3, 4, 5}
print(set1)
print('\n')

#add memeber in a set
set1.add(6)
print("After addition: ",set1)
print('\n')

#add multiple elements
set1.update([7, 8, 9])
print("After Updation: ",set1)
print('\n')

#remove items from set
set1.remove(5)
print("After deletion: ",set1)
print('\n')

#remove an item if present
set1.discard(10)
print("After Discarding ",set1)
print('\n')