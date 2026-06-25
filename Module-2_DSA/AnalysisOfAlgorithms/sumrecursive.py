#Sum of first n numbers (Recursive)
def total(n):
    if n==0:return 0
    return n+total(n-1)
print(total(10))

