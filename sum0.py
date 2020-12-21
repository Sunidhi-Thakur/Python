class ListSum:
    def sum(self, a, b):
        s = a+b
        return s



lst = []
num = int(input('Enter the number of elements: '))
for n in range(num):
    numbers = int(input('Enter elements '))
    lst.append(numbers)

flag = False
obj = ListSum()

def check():
    for i in range(0,num):
        for j in range(0,num):
            s = obj.sum(lst[i], lst[j])
            if s == 0:
                print("Element {} at position {} and element {} at position {} sum to zero".format(lst[i], i+1, lst[j], j+1))
                flag = True
                return flag

if not check():
    print("No two elemets sum to zero")

