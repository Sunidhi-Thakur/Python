def unique(list1): 
      
    list_set = set(list1) 
    unique_list = (list(list_set)) 
    for elements in unique_list: 
        print(elements) 
      
list1 = [1, 2, 1, 2, 3, 4, 3] 
print("the unique values from 1st list is") 
unique(list1)