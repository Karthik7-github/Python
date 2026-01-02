class Node:
    def __init__(self, v):
        self.val = v
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertatbegin(self, v):
        n1 = Node(v)
        if self.head is None:
            self.head = self.tail = n1
        else:
            n1.next = self.head
            self.head = n1
    
    def insertatend(self, v):
        n1 = Node(v)
        if self.head is None:
            self.head = self.tail = n1
        else:
            self.tail.next = n1
            self.tail = n1
    
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")


    def deleteatfirst(self):
        if self.head==None:
            print("List is Empty")
        else:
            self.temp=self.head
            head=head.next
            del temp
    
    def deleteatlast(self):
        if self.head is None:
            print("List is empty")
        else:
            self.temp=self.head
            

l = Linkedlist()







    
    
        