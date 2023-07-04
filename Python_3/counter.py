# Counting occurrences of n in a List
# First Implementation:
def counter(L, n):
    total = 0
    for i in L:
        if i == n:
            total+=1
    return total
# Calling counter function
print(counter({2,3,4,56,6,4,3},4)) # Output: 2
#
#
# Second Implementation: Optimized Code
def count_occurrences(L, n):
    return sum(1 for i in L if i == n)

# Example usage
print(count_occurrences([2, 3, 4, 56, 6, 4, 3], 4))  # Output: 2