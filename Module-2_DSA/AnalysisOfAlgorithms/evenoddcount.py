#Count even and odd numbers
arr=[2,5,8,7,10,13]
even=odd=0
for x in arr:
    if x%2==0: even+=1
    else: odd+=1
print("Even:",even,"Odd:",odd)
