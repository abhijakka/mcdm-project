

from itertools import product





# if  and d   :
#     print('abhi')
# else :
#     print(b)   


# arr1 = [3.5, 5.0, 5.0] 
# arr2 = [50, 100,20]

# diff = float("inf")

# for a1 in arr1:
#     for a2 in arr2:
#         if diff > abs(a1-a2):
#             diff = abs(a1-a2)
#             values = (a1, a2)

# print(values)

# import numpy as np
# myNumber = [1, 3, 4, 44, 88] 
# myList = [55,75,55] 
# myArray = np.array(myList)
# pos = (np.abs(myArray-myNumber)).argmin()
# print(myArray[pos])




myList = [4, 1, 88, 44, 3]
myNumber = 5



a=min(myList, key=lambda x:abs(x-myNumber))
print(a)