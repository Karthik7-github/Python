t=int(input())
for i in range(t):
    l=int(input())
    word=input()
    s=0
    for j in word:
        if j not in "aeiou":
            s+=1
            if s==4:
                break
            
