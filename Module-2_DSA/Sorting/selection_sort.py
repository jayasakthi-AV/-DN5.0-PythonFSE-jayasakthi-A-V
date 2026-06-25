arr=[64,25,12,22,11]
for i in range(len(arr)):
    m=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[m]:
            m=j
    arr[i],arr[m]=arr[m],arr[i]
print(arr)
