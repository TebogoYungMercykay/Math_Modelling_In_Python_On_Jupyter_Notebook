# This Method Checks if the List is Sorted
def sorted(S):
    flag = 0
    i = 1
    for i in range(1, len(S)):
        if(S[i] < S[i - 1]):
            flag = 1
        i += 1
    if(not flag):
        return True
    else:
        return False

# Creating Lists with Initial values:
G = [3,2,4,6,2]
S = [1,2,3,4,5]

# Calling the sort function
sorted(G) # Output: false
sorted(S) # Output: True