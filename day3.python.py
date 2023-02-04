Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=7
b=3
print("a=",a)
a= 7
print("b=",b)
b= 3
a=a+b
b=a-b
a=a-b
print("a=",a)
a= 3
print("b=",b)
b= 7

a=7
b=3
print("a=",a)
a= 7
print("b=",b)
b= 3
a=a*b
b=a/b
a=a/b
print("a=",a)
a= 3.0
print("b=",b)
b= 7.0

a=7
b=3
SyntaxError: multiple statements found while compiling a single statement

a=7
b=3
print(a)
7
print(b)
3
a=a^b
b=a^b
a=a^b
print(a)
3
print(b)
7

num=[1,2,3,4,5,6,7,8,9,10]
print(num)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("first ele in the list is",num[0])
first ele in the list is 1
print(num[2:5])
[3, 4, 5]
print(num[::2])
[1, 3, 5, 7, 9]
print(num[::1])
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num[0])
1
print(num[-5])
6
print(num[-10])
1
print(num[1:3])
[2, 3]
print([1::3])
SyntaxError: invalid syntax
print(num[1::3])
[2, 5, 8]
del(num[2:4])


del num[2:4]

print(del num[2:4])
SyntaxError: invalid syntax
del num[2:4]
print(num)
[1, 2, 9, 10]

n=[1,'a',"abc",[2,3,4],5.6]
print(n)
[1, 'a', 'abc', [2, 3, 4], 5.6]
print(n[3])
[2, 3, 4]
print(n[3][1])
3

len([1,2,3,4,5])
5

concatination=[1,2]+[3,4]
print(concatination)
[1, 2, 3, 4]

"gayatri"*10
'gayatrigayatrigayatrigayatrigayatrigayatrigayatrigayatrigayatrigayatri'

a in [a,e,i,o,u]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a in [a,e,i,o,u]
NameError: name 'e' is not defined
in === a in [a,e,i,o,u]
SyntaxError: invalid syntax

x=[a,e,i,o,u]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    x=[a,e,i,o,u]
NameError: name 'e' is not defined
x=['a','e','i'}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
x=['a','e']
print(a in x)
False
print(b not in x)
True

num=[1,2,3,6,8]
print(max(num))
8
print(min(num))
1

n=int(input("enter n value:"))
enter n value:10
i-1
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    i-1
NameError: name 'i' is not defined. Did you mean: 'id'?
i=1
while i<=n
SyntaxError: incomplete input

n=int(input("enter n value:"))
enter n value:10
>>> i=1
>>> while i<=n:
...     s=0
...     s=s+i
...     i+=1
... 
...     
>>> print(i)
11
>>> print(s)
10
>>> 
>>> n=int(input("enter n value:"))
enter n value:10
>>> i=1
>>> s=0
>>> while i<=n:
...     s=s+i
...     i+=1
... 
...     
>>> print(s)
55
>>> 
>>> num=[1,2,3,4,5,6,7,8,9,10]
>>> print(sum(num))
55
>>> 
