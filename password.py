n=input('enter a string: ').lower()
a=[]
d=0
s=0
confirm=input('confirm password: ').lower()
if len(n)>8 and len(n)<15:
    for i in n:
        if i in '1234567890':
            d=d+1
    
        elif i in '!@#$%^&*()_+{}|:"<>?':
            s=s+1  
else:
    print('password is not valid')
if n==confirm and d<2 and s<3:
    print('password is valid')

        

