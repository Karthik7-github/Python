# n = int(input("enter a number : "))
# s=0
# a=[]
# for i in range(1,n,1):
#     if(n%i==0):
#         a.append(i)
    
# for i in a :
#     s=s+i

# if(n==s):
#     print("PERFECT NUM")
# else:
#     print("NOT A PERFECT NUM")



for j in range(1,1000,1):
    s=0
    a=[]
    for i in range(1,j,1):
        if(j%i==0):
            a.append(i)
        
    for i in a:
        s=s+i

    if s==j:
         print(j)





    



    
   
