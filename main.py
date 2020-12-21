lst = []
m = 1
num = int(input('Enter the number of elements: '))
for n in range(num):
    numbers = int(input('Enter elements '))
    lst.append(numbers)
    m = m * lst[n]
#sum
print("Sum of elements in given list is :", sum(lst))
#largest
print("Largest element is:", max(lst)) 
#smallest
print("Smallest element is: ", min(lst))
#multiplication
print("The multiplication of elements is: ", m)