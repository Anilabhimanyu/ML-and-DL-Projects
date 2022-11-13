def first():
    print('im from first')
    return 'hi'

# init constructer example
class Divum():
    ceo='avinash gowtam'
    def __init__(self,employe):
        self.employe=employe
    def msg(self):
        return f"{Divum.ceo} recruited {self.employe}"
anil=Divum('anil')
neelu=Divum('neelu')
print(anil.msg())
print(neelu.msg())

# class variable inheritance

class Cource:
    cource='python'
class Student(Cource):
    def __init__(self,name):
        self.name=name
    def msg(self):
        return f"{self.name} took cource {Student.cource}"
santhosh=Student('santhosh')
print(santhosh.msg())
print(santhosh.__dict__)
    
class employee():
    def __init__(self,name,age,id,salary):  
       self.name = name
       self.age = age
       self.salary = salary
       self.id = id
    def earn(self):
        pass
 
class childemployee1(employee):
 
   def earn(self):
      print("no money")
 
class childemployee2(employee):
 
   def earn(self):
       print("has money")
 
c = childemployee1
c.earn(employee)
d = childemployee2
d.earn(employee)

