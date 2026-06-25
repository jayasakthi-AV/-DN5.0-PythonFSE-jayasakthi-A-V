#Frequency of elements
arr=[1,2,1,3,2,1]
freq={}
for x in arr:
    freq[x]=freq.get(x,0)+1
print(freq)
