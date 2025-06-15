import random
from add import addition
from mul import multiplication
from div import division

list = [1,2,3,4,5,6,7,8,9]

sum_item=addition(list) # sum of the list items

i = 0
while i < 3:
    if sum_item%2 == 0:
        break
    else:
        list.append(random.randint(0,9))
        sum_item=addition(list)
    i += 1

product = multiplication(list)

i = 0
while i < 3:
    if product%2 == 0:
        break
    else:
        list.append(random.randint(0,9))
        product = multiplication(list)
    i+=1

result=division(list)
print(result)





