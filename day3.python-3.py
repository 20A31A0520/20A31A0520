Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n=int(input("enter n value:"))
enter n value:1634
l=len(str(n))
n=int(n)
m=n
s=0
while(n>0):
    r=n%10
    s=s+pow(r,l)
    n=n//10

    
if(s==m):
    print("armstong no")
else:
    print("not armstong no")

    
armstong no

#0,0,7,6,14,12,21,18,24....
term=int(input("enter the term:"))
enter the term:10
if term%2==0:
    term=term//2
    print(6*(term-1))
else:
    term=term//2+1
    print(7*(term-1))

    
24

#0,0,7,6,14,12,21,18......
>>> val=int(input("enter the number: "))
enter the number: 10
>>> x=0
>>> y=
SyntaxError: incomplete input
>>> y=0
>>> for i in range(1,val+1):
...     if(i%2!=0):
...         x=x+7
...     else:
...         y=y+6
... 
>>> if(val%2!=0):
...     print('{} term in the program is {}'.format(val,x-7))
... else:
...     print('{} term in the program is {}'.format(val,y-6))
... 
...     
10 term in the program is 24
