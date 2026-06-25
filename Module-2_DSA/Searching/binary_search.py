arr=[1,2,3,4,5,6]
t=5
l,r=0,len(arr)-1
while l<=r:
 m=(l+r)//2
 if arr[m]==t:
  print(m);break
 elif arr[m]<t:l=m+1
 else:r=m-1
