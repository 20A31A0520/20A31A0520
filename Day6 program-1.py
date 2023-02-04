#object oriented programing
'''
#creating and acessing a object

class abc:
  var=10
obj=abc()
print(obj.var)

class abc:
  attribute=10
obj=abc()
print(obj.attribute)

#create a self arg and access an obj
class abc:
    attribute1=10
    def display(self):
        print("this is in class")
obj=abc()
print(obj.attribute1)
obj.display()


#usage of constructor in a method
class abc:
    def __init__(self,value):
        print("this is in class")
        self.value=value
        print("the value is ",value)
obj=abc(100)

class abc:
    class_var=0
    def __init__(self,var):
        abc.class_var +=1
        self.var=var
        print("the obj value is ",var)
        print("the class value is ",abc.class_var)
obj=abc(100)
obj=abc(101)
obj=abc(102)

# write a program to check whether the given no is even or odd by using a singlestance class obj with an attribute following a constructor.

class number:
    even=0
    def check(self,num):
        if num%2 ==0:
            self.even=1
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print(num,"is even")
        else:
            print(num,"is odd")
           
n=number()
n.even_odd(21)

class number:
    even=0
    def check(self,num):
        if num%2 ==0:
            self.even=1
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print(num,"is even")
        else:
            print(num,"is odd")
n=number()
n.even_odd(20)
         
'
class number:
    even=[]
    odd=[]
    def  __init__(self,num):
        self.num=num
        if num%2 ==0:
            number.even.append(num)
        else:
            number.odd.append(num)

n1=number(11)
n2=number(12)
n3=number(13)
n4=number(28)
n5=number(7)
print("even number list is ",number.even)
print("odd number list is ",number.odd)

'''
# use a class variable to define the values of constant pie.use this class variable to calculate
#the area and circumferce of a circle with specified radius where radius =7.5 ,pie=3.14159

class circle:
    pi=3.14159
    def __init__(self,r):
        self.r=r
    def area(self):
        return circle.pi * self.r * self.r
    def circum(self):
        return 2*circle.pi*self.r
c=circle(7.5)
print("area:",c.area)
print("circumference=",c.circum)
    







