Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import string
print(type(string.digits))
<class 'str'>
print(string.digits)
0123456789
print(string.ascii_letters)
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.find(string.lowercase,'g')!=-1)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(string.find(string.lowercase,'g')!=-1)
AttributeError: module 'string' has no attribute 'find'
print('g' in string.lowercase)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print('g' in string.lowercase)
AttributeError: module 'string' has no attribute 'lowercase'
ch='g'
print('a' <=ch <='z')
True
str1='hello'
print(dir(str1))
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

#demonstarte match() function
import re
str2='she sells sea shells at sea shore'
p1='sells'
if re.match(p1, str1):
    print("match found")
else:
    print(p1,"not present in string")

    
sells not present in string
p2='she'
if re.match(p2,str2):
    print("match found")
else:
    print(p2,"not present in string")

    
match found

import re
str1='she sells sea shells at sea shore'
p1='sea'
rep='ocean'
ns=re.sub(p1,rep,str1,1)
print(ns)
she sells ocean shells at sea shore

vowels=['a','e','i','o','u']
str='red'
for i in range(str):
    if str==vowels:
        print("vowels present")
    else:
        orint("no")

        
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    for i in range(str):
TypeError: 'str' object cannot be interpreted as an integer

import re
p=r"[aeiou]"
if re.search(p,"clue")
SyntaxError: incomplete input
if re.search(p,"clue"):
    print("vowel matched")
else:
    print("vowel not matched")

    
vowel matched

import re
p!=r"[aeiou]"
False
if re.search(p,"clue"):
    print("vowel matched")
else:
    print("vowel not matched")

    
vowel matched

#consonants
import re
p!=r"[aeiou]"
False
if re.search(p,"clue"):
    print("consonants matched")
else:
    print("consonants not matched")

    
consonants matched

str1=("listen")
str2=("silent")
n=len(str1)
m=len(str2)
sort(str1)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    sort(str1)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
sorted(str1)
['e', 'i', 'l', 'n', 's', 't']
sorted(str2)
['e', 'i', 'l', 'n', 's', 't']
if n==m:
    if sorted(str1)==sorted(str2):
        print("anagram")
    else:
        print("not an anagram")

    
anagram
else:
    
SyntaxError: invalid syntax
else:
    
SyntaxError: invalid syntax

else:
    
SyntaxError: invalid syntax

str1='listen'
str2='silent'
n=len(str1)
m=len(str2)
sortstr1=sorted(str1)
sortstr2=sorted(str2)
if n==m:
    if sortstr1==sortstr2:
        print("anagram")
    else:
        print("not an anagram")
else:
    print("not an anagram")

    
anagram

val=int(input("enter the val:"))
enter the val:15
x=0
y=0
for i in range(1,val+1):
    if(i%2!=0):
        x=x+2
    else:
        y=y+1

if(val%2!=0):
     print('{} term in the program is {}'.format(val,x-2))
else:
     print('{} term in the program is {}'.format(val,y-1))

     
15 term in the program is 14

val=int(input("enter the val:"))
enter the val:
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    val=int(input("enter the val:"))
KeyboardInterrupt

val=int(input("enter the val:"))
enter the val:16
x=0
y=0
for i in range(1,val+1):
    if(i%2!=0):
        x=x+2
    else:
        y=y+1

        
if(val%2!=0):
     print('{} term in the program is {}'.format(val,x-2))
else:
     print('{} term in the program is {}'.format(val,y-1))

     
16 term in the program is 7



size=int(input("enter size:"))
enter size:max=count=flag=0
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    size=int(input("enter size:"))
ValueError: invalid literal for int() with base 10: 'max=count=flag=0'

size=int(input("enter size:"))
enter size:6
max=count=flag=0
bininput=input()
101000
arr=list(x)
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    arr=list(x)
TypeError: 'int' object is not iterable

size=int(input("enter value:"))
enter value:6
max=count=flag=0
x=input()
101000
arr=list(x)
for i in range(0,size)
SyntaxError: incomplete input
for i in range(0,size):
    if arr[i]=='1':
        count=count+1
        flag=1
    elif (arr[i]=='0' and flag ==1):
...         count=0
...         flag=0
...     if count>max:
...         max=count
... 
...         
>>> print(max)
1
>>> 
>>> size=int(input("enter value:"))
enter value:9
>>> max=count=flag=0
>>> x=input()
101111110
>>> arr=list(x)
>>> for i in range(0,size):
...     if arr[i]=='1':
...         count=count+1
...         flag=1
...     elif (arr[i]=='0' and flag ==1):
...         count=0
...         flag=0
...     if count>max:
...         max=count
... 
...         
>>> print(max)
6
>>> 
