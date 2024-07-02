'''class Person:
    
    x=4
    print(x)

P1=Person()
print(P1.x) '''


'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        
class Student:
        x=90
        def __init__(self, name, age):
           self.name = name
           self.age = age
           print(person1.age)
           
        
person1 = Person("Alice", 30)
print(person1.name)
Student2=Student("Monica",92)'''





'''class person:
    
    def __init__(self,name,age):
        self.personname = name
        self.personage=age
        self.sonika()
    
    def sonika(self) :
       print("Hello world")
    
    
    
p1=person("sonika",23)   ''' 


'''class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    print("sonika")

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()'''



'''Create a base class called Animal with a method make_sound() that prints "Some generic sound". 
Then, create two subclasses Dog and Cat. Dog should override the make_sound() method to print "Woof!", 
and Cat should override the method to print "Meow!".Demonstrate inheritance by creating instances of both 
Dog and Cat classes and calling the make_sound() method on each instance.'''
       
        
'''class Animal:
    def make_sound(self):
        print("generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Creating instances
A = Animal()
D = Dog()
C = Cat()

# Calling methods
A.make_sound()  # Output: generic sound
D.make_sound()  # Output: Woof!
C.make_sound()  # Output: Meow!'''      
        
        
        
        
'''Create a base class called Vehicle with attributes brand and model, 
 and a method display_info() that prints the brand and model of the vehicle.
 Then, create a subclass called Car that inherits from Vehicle and adds an attribute year 
 representing the manufacturing year of the car. Also, add a method start_engine() to the Car class that 
 prints "Engine started!".  '''

'''class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)
        self.year = year

    def start_engine(self):
        print("Engine started!")

# Creating an instance of Car
car = Car("Toyota", "Camry", 2020)

# Calling methods
car.display_info()  # Output: Brand: Toyota, Model: Camry
car.start_engine()  # Output: Engine started!'''

'''class vehicle:
    
    def vehicle3(self):
        print("Benz")

    def vehicle4():
        print("audi")
        
        
class vehicle2(vehicle) :
   
    def vehicle5():
        
       print("mercedes")
                
        
v=vehicle()  
v.vehicle3()
      
v2=vehicle2()
v2.vehicle5()'''
  
"""Suppose you're designing a simple game where different characters have different abilities.
 Implement a Python program using inheritance where there's a base class Character with a method attack()
 that prints "Character attacks!". Then, create two subclasses Warrior and Mage, each with their own attack() method. 
 The attack() method for Warrior should print "Warrior swings sword!", and for Mage, it should print "Mage casts a spell!"."""

'''class character:
    
    def attack(self):
        print("character attacks!")
    
class Warrior(character):

    def attack(self):
        print("Warrior swings sword!")
       
class Mage:

     def attack(self):
         print("Mage casts a spell!")
              
     
c1=character()
c1.attack()
     
c2=Warrior()
c2.attack()
             

c3=Mage()
c3.attack()'''
     
'''import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5 * self.base * self.height

# Example usage:
rectangle = Rectangle(5, 4)
print("Area of rectangle:", rectangle.area())

circle = Circle(3)
print("Area of circle:", circle.area())

triangle = Triangle(4, 6)
print("Area of triangle:", triangle.area())'''




'''try:
    # Code that might raise an exception
    result = 10 / 2
except ZeroDivisionError:
    # Handle specific exception
    print("Cannot divide by zero")
else:
    # Executed if no exception occurred
    print("Division successful")
finally:
    # Always executed, for cleanup actions
    print("Exiting try-except block")'''
    
'''import datetime as dt

print(dt.datetime.now())

x=dt.datetime.now()
print(x.time())
print(x.date())   
print(x.year) '''


'''sum=0
for i in  range(1,11) :
   
    if (i%2==0):
        print(i)
        sum=sum+1
        
print("the total even number is",sum)'''
                                                                                                                                                                            

 

'''==================================================================================================================================='''


'''class rectangle:
    
    def __init__(self,length,width):
        
        self.length=length
        self.width=width


    def area(self):
        
        return self.length * self.width

    def perimeter(self):
        
         return  2*(self.length + self.width)


x=float(input())
y=float(input())

r=rectangle(x,y)

print(r.area())
print(r.perimeter())'''


'''==================================================================================================================================='''

'''class shape:
    
     def rectangle(self,a,b):
         return a*b
     def circle(self,a,b):
         return a+b
     
        
shape=shape() 
print(shape.rectangle(2,4)) 
print(shape.circle(2,4))  '''


'''==================================================================================================================================='''    



'''class Shape:
     def__init__(self, a, b):
        self.a = a
        self.b = b

    def rectangle_area(self):
        return self.a * self.b

    def circle_circumference(self):
        return 2 * 3.14 * self.a  # Assuming 'a' is the radius

# Creating an instance of Shape
shape = Shape(3, 4)
print(shape.rectangle_area())
print(shape.circle_circumference())'''



'''a=10
b=20
c=a
a=b
b=c
print(a,b)'''

'''a=10
b=20
a = a + b
b = a - b
a = a - b
print(a,b)'''



'''a="sonika"
count=0
for i in a:
    if i in"aeiou":
          count+=1
print(count)   '''    

'''v=[3,4,5,6,6]
v.append(4)
v.pop(2)``````````````````````````````````````````````
print(v)'''

x=(3,45,6,8,7,6)
print(x.count(6))

print(x.index(3))

 

a=8
b=8
for i in range(8,9):
    for j in range(i):
        a=a-1
    b=b-2
print(str(b))
print(str(a))
    





























      
     
        
     
        
     
        
     
        
     
        
     
        
     
        
     
        
     
        
     
        
        
        
        
        
        
    
