Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a,b,c=10,20,30
print(b,c,a)
20 30 10
print(b,c,a,sep='?')
20?30?10

print('09','12','2016', sep='-')
09-12-2016
print('A','B','C',SEP='-')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print('A','B','C',SEP='-')
TypeError: 'SEP' is an invalid keyword argument for print()
print('A','B','C',sep='-')
A-B-C

apple=100
banana=200
pineapple=300
print(banana)
200
print(apple)
100
print(apple,banana,pineapple)
100 200 300
print(apple,end=' ')
100 
print(banana,end=' ')
200 

x,y,z=input("enter a three values: ").split()
enter a three values: 100 200 300
print("total no of students: ",x)
total no of students:  100
print("no of boys: ",y)
no of boys:  200
print("no of girls: ",y)
no of girls:  200
x,y,z=input("enter a three values: ").split('&')
enter a three values: 1000 2000 * 3000 - 4000 & 5000 6000 ( 7000 + 8000 & 90000
print("total no of students: ",x)
                                                            
total no of students:  1000 2000 * 3000 - 4000 
print("no of boys: ",y)
                                                            
no of boys:   5000 6000 ( 7000 + 8000 
print("no of girls: ",z)
                          
no of girls:   90000


x,y,z=input("enter a three values: ").split('0')
                          
enter a three values: 1002003
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    x,y,z=input("enter a three values: ").split('0')
ValueError: too many values to unpack (expected 3)
x,y,z=input("enter a three values: ").split('0')
                          
enter a three values: 100
print("total no of students: ",x)
                          
total no of students:  1
print("no of boys: ",y)
                          
no of boys:  
print("no of girls: ",z)
                          
no of girls:  
x,y,z=input("enter a three values: ").split('0')
                          
enter a three values: 20304
print("total no of students: ",x)
                          
total no of students:  2
print("no of boys: ",y)
                          
no of boys:  3
print("no of girls: ",z)
                          
no of girls:  4

CONTROL STATEMENTS
                          
SyntaxError: incomplete input

email="gayatri@gmail.com"
                          
pwd=123456
                          
cemail=input("enter the email:")
                          
enter the email:vishnu@gmail.com
cpwd=input("enter the email:")
                          
enter the email:123456
if(email==cemail and pwd==cpwd):
    print("login successfull")
else:
    print("login unsuccessfull")

    
login unsuccessfull

email="gayatri@gmail.com"
                          
pwd=123456
SyntaxError: multiple statements found while compiling a single statement
cemail=input("enter the email:")
enter the email:gayatri@gmai.com
cpwd=int(input("enter the email:"))
enter the email:123456
if(email==cemail and pwd==cpwd):
    print("login successfull")
else:
    print("login unsuccessfull")

login unsuccessfull

a=5
b=6
if(a==b):
    print("yes")
else:
    print("no")

    
no
a=5
b=5.0
if(a==b):
    print("yes")
else:
    print("no")

    
yes

a=5
b=true
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    b=true
NameError: name 'true' is not defined. Did you mean: 'True'?
a=5
b=True
if(1==b):
    print("yes")
else:
    print("no")

    
yes

x=int(input("enter x value:"))
enter x value:49
if(x%7==0):
    print("divisible")
else:
    print("not divisible")

    
divisible

email="gayatri@gmail.com"
pwd=123456
cemail=input("enter the email:")
enter the email:gayatri@gmail.com
cpwd=int(input("enter the pwd:"))
enter the pwd:123456
if(email==cemail and pwd==cpwd):
    print("login successful")
elif(email!=cemail and pwd==cpwd):
    print("login failed due to mail")
elif(email==cemail and pwd!=cpwd):
    print("login failed due to pwd")
elif(email!=cemail and pwd!=cpwd):
    print("login failed due to mail and pwd")

    
login successful

email="gayatri@gmail.com"
pwd=123456
SyntaxError: multiple statements found while compiling a single statement
email="gayatri@gmail.com"
pwd=123456
cemail=input("enter the email:")
enter the email:gayatri@gmail.com
pwd=123456
cpwd=int(input("enter the pwd:"))
enter the pwd:123456
if(email==cemail and pwd==cpwd):
    print("login successful")

    
login successful

email="gayatri@gmail.com"
pwd=123456
KeyboardInterrupt
cemail=input("enter the email:")
enter the email:gayatri@gmail.com
cpwd=int(input("enter the pwd:"))
enter the pwd:123456
otp=1256
if(email==cemail and pwd==cpwd):
    cotp=int(input("enter otp:"))

    
enter otp:1245
   if(cotp=int(input("enter otp:"))):
       
SyntaxError: unexpected indent

email="gayatri@gmail.com"
pwd=123456
otp=1256
cemail=input("enter the email:")
enter the email:gayatri@gmail.com
cpwd=int(input("enter the pwd:"))
enter the pwd:123456
if(email==cemail and pwd==cpwd):
    cotp=int(input("enter otp:"))
    if(cotp==otp):
        print("order successfull")
    else:
        print("order unsuccessfull")
elif(email!=cemail and pwd==cpwd):
    print("login failed due to mail")

enter otp:1258
order unsuccessfull

a="gayatri"
print('y' not in a)
False
print('y' in a)
True
print(a[3])
a

for(i in range())
SyntaxError: incomplete input
for(i in range()):
    
SyntaxError: incomplete input
for(i in range(1,10)):
    
SyntaxError: incomplete input
for i in range(1,10):
    print(i)

    
1
2
3
4
5
6
7
8
9
for i in range(10,1):
    print(i,end="*")

    

for i in range(1,10,-1):
    print(i)

    

for i in range(10,0,-1):
    print(i)

    
10
9
8
7
6
5
4
3
2
1
for i in range(10,1,-1):
    print(i,end="*")

    
10*9*8*7*6*5*4*3*2*
for i in range('a','z',1):
    print(i,end=" ")

    
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    for i in range('a','z',1):
TypeError: 'str' object cannot be interpreted as an integer
for i in range(97,122):
    print(chr(i),end=" ")

    
a b c d e f g h i j k l m n o p q r s t u v w x y 

for i in range(97,122):
    print(i)

    
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121

for i in range(97,122)
SyntaxError: incomplete input
for i in range(97,122):
    if(chr(i)=='a','e','i','o','u'):
        print(chr(i))

        
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
for i in range(65,91):
    if(i==65 or i==69 or i==73 or i==79 or i==85)
    
SyntaxError: incomplete input
for i in range(65,91):
    if(i==65 or i==69 or i==73 or i==79 or i==85):
        print(chr(i),end=" ")

        
A E I O U 
for i in range(65,91):
    if(i!=65 or i!=69 or i!=73 or i!=79 or i!=85):
...         print(chr(i),end=" ")
... 
...         
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
>>> for i in range(65,91):
...     if(i!=65 and i!=69 and i!=73 and i!=79 and i!=85):
...         print(chr(i),end=" ")
... 
...         
B C D F G H J K L M N P Q R S T V W X Y Z 
>>> for i in range(91,64,-1):
...     if(i!=65 and i!=69 and i!=73 and i!=79 and i!=85):
...         print(chr(i),end=" ")
... 
...         
[ Z Y X W V T S R Q P N M L K J H G F D C B 
>>> for i in range(91,64,-2):
...     if(i!=65 and i!=69 and i!=73 and i!=79 and i!=85):
...         print(chr(i),end=" ")
... 
...   
[ Y W S Q M K G C 
>>> 
>>> for i in range(91,64,-2):
...     if(i!=65 and i!=69 and i!=73 and i!=79 and i!=85):
...         print(chr(i),end=" ")
... 
...   
[ Y W S Q M K G C
for i in range(91,64,-2):
...     if(i!=65 and i!=69 and i!=73 and i!=79 and i!=85):
...         print(chr(i),end=" ")




  
