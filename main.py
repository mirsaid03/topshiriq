import numpy as np
data1 =np.loadtxt("data1.txt",dtype=int)
w=[0]*(len(data1[0])-1)
summa=0
s=0
stop=0
while True:
    s+=1
    i=s%4-1
    summa=0
    for j in range(len(data1[i])-1):
        summa +=(w[j]*data1[i][j])
    if summa>=0:
            k=1
    else:
            k=0
    if summa>=0 and k!=data1[i][-1]:
        for j in range(len(data1[i])-1):
                w[j]=w[j]-data1[i][j]
                stop=0
    elif summa<0 and k!=(data1[i][-1]):
        for j in range(len(data1[i])-1):
            w[j]=w[j]+data1[i][j]
        stop=0
    else:
        stop+=1
    if stop==len(data1):
        break
print(w)
print(s)
for i in range(len(data1[i])-1): 
    summa+=int(input('x:'))*w[i]
if summa>=0:
    print("Yangi obyekt toq sinfga tegishli")
else:
    print("Yangi obyekt juft sinfgategishli")