# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 09:58:22 2020

@author: ADMIN
"""

def square_of_numbers(num1, num2, num3,
                      num4):
    return num1**2, num2**2, num3**2, num4**2
values = square_of_numbers(
    1, 2, 3, 4
    )
print(values)

dict_of_people = {
    "Nam": 20,
    "Ngọc": 25,
    "Bình": 22
}
for x in dict_of_people:
    #print ("Số tuổi của", x, "là:", dict_of_people[x])
    #print ("Số tuổi của %s là %d" % (x, dict_of_people[x]))
    #print ("Số tuổi của {0} là {1}".format(x, dict_of_people[x]))
    print(f"Số tuổi của {x} là {dict_of_people[x]}")
    
x, y, z = 1, 2, 3
total = (x +
         y +
         z
         )
print (total)         

#Tính toán ma trận vói python
