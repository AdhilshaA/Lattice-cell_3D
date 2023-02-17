import math as m
from numpy import linalg
p = []
p.append((1,2,3))
p.append((4,5,6))
p.append((p[-1][0]+3,p[-1][1]+3,p[-1][2]+3))

i = 0
if i not in p:
    print("hi")

k = [[],[]]
for i in range(2):
    k[i].append(i)
print(k)

a = [2,2,m.sqrt(8)]
print(a)
print(a/(linalg.norm(a)))

for i in range(10) and i // 2 == 1:
    print('hiii')