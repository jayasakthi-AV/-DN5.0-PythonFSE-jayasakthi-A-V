
arr=[4,2,7,1]
p=arr[-1]
print([x for x in arr[:-1] if x<=p]+[p]+[x for x in arr[:-1] if x>p])
