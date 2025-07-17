# Single Level Inheritance
print("************** Single Inheritance **************")

class A:
  def display(self):
    print("Display function of Class A")

#Use the Person class to create an object, and then execute the printname method:
class B(A):
  def print(self):
    print("Print function of Class B")

b1=B()
b1.display()
b1.print()

# Multiple Inheritance
print("************** Multiple Inheritance **************")
class A1:
  def display1(self):
    print("Display methord of class 1")
class B1:
  def print1(self):
    print("Display methord of class 2")

class C1 (A1,B1):
  def hello(self):
    print("Display methord of Child Class")

c1= C1()
c1.display1()
c1.print1()
c1.hello()

# MultiLevel inheritance
print("************** MultiLevel Inheritance **************")

class A2:
  def display2(self):
    print("Display methord from Class A2")
class B2(A2):
  def print2(self):
    print("Display methord from class B2")
class C2(B2):
  def hello2(self):
    print("Display methord from class C2")

c21=C2()
c21.display2()
c21.print2()
c21.hello2()

# Herchical inheritance
print("************** herachical Inheritance **************")

class A3:
  def display3(self):
    print("Display methord from class A3")
class B3(A3):
  def print3(self):
    print("Display methord from class B3")
class C3(A3):
  def hello3(self):
    print("Display methord from class C3")

b31=B3()
b31.display3()
b31.print3()

c31=C3()
c31.display3()
c31.hello3()

print("******* Polymorphism ********")
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()

make_sound(dog)   
make_sound(cat)   

print("******** Method Overriding ********")
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start(self):
        print("Car started")

v = Vehicle()
c = Car()

v.start()   
c.start()   