# task 18
import random
# mlist = [1,2,3,4,5,5,6,7] # учебный массив
mlist=[]
print('имеющийся список:')
for i in range(30):
     x = random.randint(1,100)
     mlist.append(x)

print(*mlist)
FIND = 21
print(FIND, '- предложенное для поиска число')
pos = ""
min = 100
for j in range(len(mlist)):
    if (abs(mlist[j]-FIND) < min):
        pos = j
        min = abs(mlist[j]-FIND)
print(f"{FIND} ближе всего к числу {mlist[pos]}, находящемуся на позиции {pos+1}")
