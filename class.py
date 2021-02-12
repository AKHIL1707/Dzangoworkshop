"""#Attributes

class Student:
    roll_number=0 #class Attributes
    name=""
    def disp_details(self):
        return self.roll_number,self.name

obj=Student()
print(obj.disp_details())"""
'''
class Student:
    roll_number=0 #class Attributes
    name=""
    def disp_details(self,roll_number,name):
        return roll_number,name
    def check(self):
        return self.roll_number,self.name

obj=Student()
print(obj.disp_details(12,"akhil"))
print(obj.check())'''
'''

#Local,Global and class Variables
a = 1  #global
b = 2
class MyClass():
  i=3
  j=4#class variables
  def method(self,m,n):
      print("local m,n",m,n)
      print("class variabls",self.i,self.j)
      print("Global variables",a,b)
    
variable=MyClass()
variable.method(10,20)


#Local,Global and class Variables with same names
a = 1  #global
b = 2
class MyClass():
  a=3
  b=4#class variables
  def method(self,a,b):
      print("local m,n",a,b)
      print("class variabls",self.a,self.b)
      print("Global variables",globals()['a'],globals()['b'])
    
variable=MyClass()
variable.method(10,20)'''
'''
class Student():
    name=""
    branch=""
    def __init__(self,name,branch)
    self.name=name
    self.branch=branch
   
    def disp(self):
        return self.name,self.branch
obj =Student('akhil','cse')
print(obj.disp())

#__str__
class TempClass():
    def __str__(self):
        return "this is temporary class"
d=TempClass()
print(d)'''
'''
#,,,,,,,,,,,,,,,,Inheritance,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
class A():
    pass
class parent():
    pass
class child(parent):
    pass 

class A():
    def m1(self):
        return "class A method"
class B(A):
    def m2(self):
        return "class B method"
a=A()
b=B()

class parent():
    def m1(self):
        return "parent m1"
class child(parent):
    def m2(self):
        super().m1()
        return "child m2"
a=parent()
obj2 = child()
print(a.m1())
print(obj2.m2())

 
#Accessing Attributes from parent class Using Super(),,,,,,,,,,,,,,,,,,,,,,,,,,
class Class1:
    a=100
    b=122
class Class2(Class1):
    def m1(self):
        result = super().a+super().b
        return result
e=Class2()
print(e.m1())

class Class1:
    a=100
    b=122
class Class2(Class1):
 a=1
 b=3
    def m1(self,a,b):
        print(a,b)
        print(self.a,self.b)
        print(super().a,super().b)
e=Class2()
e.m1(99,55)


#multi level inheritance,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
class A():
    pass
class B(A):
    pass
class C(B):
    pass

#Multiple Inheritance,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
class parent1():
    pass
class parent2():
    pass
class child(parent1,parent2):
    pass

#Hierarical inheritance,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
class MyParent():
    pass
class Mychild(MyParent):
    pass
class MyChild2(Myparent):
    pass  '''

class A():
    a=12
    b=13
class B(A):
    super().a
    super().b
class C(B):
    def m1(self,a,b):
       super().a
       super().b
d1=A()
d2=B()
d3=C()
print(d3.m1())
 




        







