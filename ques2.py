class Student:
    def __init__(self,first,last):
        self.first=first
        self.last=last

    def emailGenerator(self):
        self.email=self.first.lower()+'_'+self.last.lower()+"@gmail.com"


std= Student(input("Enter first name: "),input("Enter last name: "))
std.emailGenerator()
print("E-mail Id: " +std.email)
