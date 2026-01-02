class Node:
    def __init__(self, v):
        self.val = v
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = self.tail = None

    def atfront(self, v):
        n1 = Node(v)
        if self.head is None:
            self.head = self.tail = n1
        else:
            n1.next = self.head
            self.head = n1

    def atlast(self, v):
        n1 = Node(v)
        if self.head is None:
            self.head = self.tail = n1
        else:
            self.tail.next = n1
            self.tail = n1   # 🔥 FIX: update tail here

    def deleteatfirst(self):
        if self.head is None:
            print("Linked list is Empty")
            return
        else:
            temp = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            del temp

    def deleteatlast(self):
        if self.head is None:
            print("Linked list is Empty")
            return
        elif self.head == self.tail:
            temp = self.head
            self.head = self.tail = None
            del temp
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            del self.tail
            self.tail = temp
            self.tail.next = None

    def deletevalue(self,v):
        if self.head is None:
            print("Linked list is Empty")
            return
        if self.head.val==v:
            self.head=self.head.next
            return
        temp=self.head
        while temp.next is not None and temp.next.data!=v:
            temp=temp.next
        if temp is not None and temp.next is not None:
            temp.next=temp.next.next

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.val, " -> ", end="")
            temp = temp.next
        print(None)



l = Linkedlist() 
while(1):
    print("1.add at first \n2.add at last\n3.delete at first\n4.delete at last\n5.print list\n6.Exit")
    print("Enter choice : ",end="")
    n=int(input())
    if(n==1):
        print("Enter Value : ",end="")
        e=int(input())
        l.atfront(e)
    elif(n==2):
        print(f"Enter Value : ",end="")
        e=int(input())
        l.atlast(e)
    elif(n==3):
        l.deleteatfirst()
    elif(n==4):
        l.deleteatlast()
    elif(n==5):
        l.printlist()
    elif(n==6):
        exit()
    else:
        print("Enter correct option!")