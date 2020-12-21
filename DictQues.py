# add a key to a dictionary
dict1 = {1:'one', 2:'two'} 
print("Current Dict is: ", dict1) 
dict1.update({3:'three'}) 
print("Updated Dict is: ", dict1) 
print('\n')

# Concatenate dictionaries
dict2={4:'four', 5:'five'}
dict3={}
for keys in (dict1, dict2): 
    dict3.update(keys)
print(dict3)
print('\n')


# key exits or not
def checkKey(dict3, key): 
      
    if key in dict3.keys(): 
        print("Key exists") 
        print('\n')

    else: 
        print("Key does not exists")
        print('\n')

key = int(input("Enter key: "))
checkKey(dict3, key) 
  
key = int(input("Enter key: "))
checkKey(dict3, key) 
