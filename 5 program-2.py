'''
from time import*
t1=perf_counter()
p=sum=0
while i<1000000:
    sum+=1
    i+=1
sleep(0)
t2=perf_counter()
print("execution time=%fseconds"%(t2-t1))


def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,b,c)
        if a:
            c.append(a.pop())
        hanoi(n-1,b,a,c)
a=[1,2,3,4]
b=[]
c=[]
print("before puzzle")
print(a,b,c)
hanoi(len(a),a,b,c)
print("after puzzle")
print(a,b,c)
'''
from datetime import*
d=date.today()
print(d)
d= date(2023,2,3)
for x in range(1,10):
    nextdate = d +timedelta(days=x)
    print(nextdate) 
def fact():
    if n==1:
        fact=1
    else:
        f=f*(n-1)*n
while(n!=0):
     r=a%10
s=s+f(n)
n=n//10
if(n==s):
    print("krishnamurty no")
else:
    print("not")
 
