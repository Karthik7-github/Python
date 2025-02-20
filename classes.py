# class Employee:
#     def setdetails(self):
#         self.id=int(input())
#         self.name=input()
#         self.salary=int(input())
#         self.doj=input()

#     def getdetails(self):
#         print("Employee id ",self.id)
#         print("Employee name ",self.name)
#         print("Employee salary ",self.salary)
#         print("Employee doj",self.doj)
#     def Bonus(self):
#         if(self.salary>50000):
#             inc=self.salary*0.2
#             self.salary=self.salary+inc

# a=Employee()
# a.setdetails()
# a.Bonus()
# a.getdetails()



class student:
    def setstudent(self):
        self.id=int(input())
        self.name=input()
        self.marks=list(map(int,input().split()))
    def getstudent(self):
        print("student name : ",self.name)
        print("student id : ",self.id)
        print("student marks : ",self.marks)
        print("student grade : ",self.grade)
    def grade(self):
        total=sum(self.marks)
        avg=total/5
        if(avg>90):
            self.grade="A"
        elif(avg>80):
            self.grade="B"

a=student()
a.setstudent()
a.grade()
a.getstudent()