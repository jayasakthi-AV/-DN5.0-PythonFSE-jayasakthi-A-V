import heapq
arr=[9,4,7,1]
heapq.heapify(arr)
res=[]
while arr: res.append(heapq.heappop(arr))
print(res)
