##Прога будет выдавать код замка, если значения на начальных кубиках будут одинаковыми(например, 3-3, 4-4 и тд)
##но не всегда(иногда может не выдавать), так как я использую рандом, и числа в ячейках могут быть <1 или >6
from random import *
a =[0]*10
c = randint(0,1)
d = randint(3,9)
a[c] = int(input('Первый кубик: '))
a[d] = int(input('Второй кубик: '))

print(a)
for i in range(2,10):
    
    if a[i-2]!=0 and a[i-1] ==0 and a[i] == 0:    
        a[i-1] = 10 - a[i-2] - randint(1, 6)
        a[i] = 10 - a[i-2] -a[i-1]
    elif a[i-2]!=0 and a[i-1] !=0 and a[i] == 0:
         a[i] = 10 - a[i-2] - a[i-1]
    elif a[i-2]==0 and a[i-1] !=0 and a[i] == 0:
        a[i-2] = 10 - a[i-1] - randint(1, 6)
        a[i] = 10-a[i-1]-a[i-2]
         
    elif a[i-2] !=0 and a[i-1] == 0 and a[i] !=0:
        a[i-1] = 10 - a[i-2] - a[i]

f = True
for i in range(len(a)):
    if (a[i] > 6 or a[i] <1):
        f = False
        break
if f == True:
    if a[d] + a[d-1] +a[d-2] != 10:
        print('нет такого кода')
    else:
        print(a)
else:
    print('нет такого кода')
    
      

