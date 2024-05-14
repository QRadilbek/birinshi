import random
start=1
stop=7
random_num = random.randint(1,100)
print(random_num)
while start<=stop:
    x=int(input('x= '))
    if random_num<x:
        x=int(input('ulken san jaz'))
    if random_num>x:
        x=int(input('kishi san jaz'))
        break
    else:
        print('utildin')
