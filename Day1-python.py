Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print(3078)
3078
print("gayatri")
gayatri
print(chr(3078))
ఆ

import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

x,y,z="orange","banana","cherry"
print(x,y)
orange banana
print(x,z)
orange cherry

x=y=z="orange"
print(x,y,z)
orange orange orange

x='how'
y='are u'
print(x+y)
howare u

X='john'
x='John'
print(X)
john
print(x)
John

x=5
y="the answer is"
print(x+y)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(x+y)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(y,x)
the answer is 5

name=int(input("enter name:"))
enter name:gayatri
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    name=int(input("enter name:"))
ValueError: invalid literal for int() with base 10: 'gayatri'
name=input("enter name:")
enter name:gayatri
age=int(input("enter age:"))
enter age:20
print(name,age)
gayatri 20

print(chr(3095)+chr(3134)+chr(3119)+chr(3073)+chr(3108)+chr(3135))
గాయఁతి


x=5
y=3
print(x//y)
1
print(x/y)
1.6666666666666667
print(x%y)
2
x+=10

a=5
a+=10
print(a)
15
a*=10
print(a)
150
a/=5
a**=2
print(a)
900.0
a//=2
print(a)
450.0

a=10
b=5
c=a&b
d=a/b
e=a^b
f=~e
print(c)
0
print(d)
2.0
print(e)
15
print(f)
-16
print(a<<b)
320
>>> print(a>>b)
0
>>> print(a>b and a>c)
True
>>> print(a<b and a>c and a>d)
False
>>> 
>>> a=5
>>> b=10
>>> print(a if a>b else b)
10
>>> 
>>> a=1000
>>> b=2000
>>> c=-500
>>> d=4000
>>> e=1500
>>> print(a if (a<b and a<c and a<d and a<e)else (b if b<c and b<d and b<e) else c if(c<d and c<e) else d if (d<e)else e)
SyntaxError: expected 'else' after 'if' expression
>>> print(a if (a<b and a<c and a<d and a<e)else b if (b<c and b<d and b<e) else c if(c<d and c<e) else d if (d<e)else e)
-500
>>> print(a if (a>b and a>c and a>d and a>e)else (b if b>c and b>d and b>e) else c if(c>d and c>e) else d if (d>e)else e)
SyntaxError: expected 'else' after 'if' expression
>>> print(a if (a>b and a>c and a>d and a>e)else b if (b>c and b>d and b>e) else c if(c>d and c>e) else d if (d>e)else e)
4000
