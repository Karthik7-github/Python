def selectionsort(arr):
    for i in range(len(arr)):
        mid_ind=i
        for j in range(i+1,len(arr)):
            if arr[j]>arr[mid_ind]:
                          mid_ind=j
        arr[i],arr[i+1]=arr[i+1],arr[i]
        print(arr)

arr=list(map(int,input().split()))
print("Before sort : ",arr)
selectionsort(arr)
print("After sort : ",arr)