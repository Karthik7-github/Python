class person:
    def set_details(self,d,n):
        self.id=d
        self.name=n
    def print_details(self):
        print("id :",self.id)
        print("Name : ",self.name)

class Employee(person):
    def set_detail(self,d,s):
        self.doj=d
        self.salary=s

    def print_child_details(self):
        print("date of joining : ",self.doj)
        print("salary : ",self.salary)

    obj.set_detail(10,20)
    obj.print_child_details()
