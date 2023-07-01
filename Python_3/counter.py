# Counting occurrences of n in a List
def counter(L, n):
    total = 0
    for i in L:
        if i == n:
            total+=1
    return total
# Calling counter function
counter({2,3,4,56,6,4,3},4) # Output: 2