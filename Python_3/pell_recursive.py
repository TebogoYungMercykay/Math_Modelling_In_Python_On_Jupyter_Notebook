# Recursive function
def pell_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 2 * pell_recursive(n - 1) + pell_recursive(n - 2)
# Calling the Recursive function
pell_recursive(20)