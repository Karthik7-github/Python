n=int(input("Enter the number of patients: "))
x=[]
for i in range(n):
    age=int(input("Enter the age of the patient: "))
    x.append(age)
s=0
for i in range(n):
    if x[i] < 17:
        print(f"fees is {200}")
        s+= 200
    elif x[i] < 40 and x[i] > 17:
        print(f"fees is {400}")
        s+= 400
    else:
        print(f"fees is {300}")
        s+= 300

print(f"Total fees is {s}")

