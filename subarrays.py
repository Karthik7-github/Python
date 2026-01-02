# # def print_subarrays(arr):
# #     n = len(arr)
# #     for i in range(n):
# #         for j in range(i, n):
# #             print(arr[i:j+1])

# # arr = [1, 2, 3]
# # print_subarrays(arr)

# # s=input()
# # v='aeiouAEIOU'
# # l=[]
# # m=[]
# # for i in range(len(s)):
# #     if s[i] in v:
# #         l.append(int(i))
# #         m.append(s[i])
# # m=sorted(m)
# # k=0
# # for i in range(len(s)):
# #     if i in l:
# #         s[i]=m[k]
# #         k+=1
# # print(s)

# s = input()
# v = 'aeiouAEIOU'
# l = []
# m = []

# # Collect indices and vowels
# for i in range(len(s)):
#     if s[i] in v:
#         l.append(i)
#         m.append(s[i])

# # Sort vowels
# m.sort()
# k = 0

# # Convert string to list for mutability
# s = list(s)

# # Replace vowels with sorted ones
# for i in l:
#     s[i] = m[k]
#     k += 1

# # Join back into string
# print("".join(s))

arr=[23,1,4,6,3,6,8,2,1]

for i in range(1,len(arr)):
    curr=arr[i]
    j=i-1
    while(j>=0 and arr[j]>=curr):
        