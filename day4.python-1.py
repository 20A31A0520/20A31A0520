Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
str1="india"
str2="bharath"
print(str1+str2)
SyntaxError: multiple statements found while compiling a single statement

str1="india"
str2="bharath"
print(str1+str2)
indiabharath
str1="india"
str2=input("enter a name")
enter a namejai hind
str +=str2
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    str +=str2
TypeError: unsupported operand type(s) for +=: 'type' and 'str'
str+=str2
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    str+=str2
TypeError: unsupported operand type(s) for +=: 'type' and 'str'
str1="india"
str2=input("enter a name")
enter a namejai hind
str1 +=str2
print(str)
<class 'str'>
print(str1)
indiajai hind
#reptetion
ste1="india"
str1="india"
print(str*10)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(str*10)
TypeError: unsupported operand type(s) for *: 'type' and 'int'
print(str1*10)
indiaindiaindiaindiaindiaindiaindiaindiaindiaindia
print(str*10,end="")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(str*10,end="")
TypeError: unsupported operand type(s) for *: 'type' and 'int'
print(str1 *10,end="")
indiaindiaindiaindiaindiaindiaindiaindiaindiaindia
text="india"
index=0
for i in text:
    print("text[",index,"]=",i)
    index +=1

...     
... text[ 0 ]= i
... text[ 1 ]= n
... text[ 2 ]= d
... text[ 3 ]= i
... text[ 4 ]= a
... text='india is great'
... print(text.tittle())
... Traceback (most recent call last):
...   File "<pyshell#27>", line 1, in <module>
...     print(text.tittle())
... AttributeError: 'str' object has no attribute 'tittle'. Did you mean: 'title'?
... text='india is great'
... print(text.title())
... India Is Great
... text='india is great'
... print(text.split())
... ['india', 'is', 'great']
... print(text.title())
... India Is Great
... print(text.split())
... ['india', 'is', 'great']
... text='india is great'
... print(text.swapcase())
... INDIA IS GREAT
... print('-'.join(['india','is','greate']))
... india-is-greate
... str1 ='donkey'
... print(list(enumerate(str1)))
... [(0, 'd'), (1, 'o'), (2, 'n'), (3, 'k'), (4, 'e'), (5, 'y')]
>>> str1='66'
>>> print(str1,zfill(4))
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print(str1,zfill(4))
NameError: name 'zfill' is not defined
>>> str1='66'
>>> print(str1.zfill(4))
0066
>>> str="navika"
>>> print(str.upper())
NAVIKA
>>> #slicing program
>>> str1='india'
>>> print(str[1::5])
a
>>> str1='india'
>>> print(str1[1::5])
n
>>> str1='india'print(str1[1::5])
SyntaxError: invalid syntax
>>> str1='india'
>>> print(str1[1:5])
ndia
>>> print(str1[::])
india
>>> print(str1[:])
india
>>> print(str1[::-1])
