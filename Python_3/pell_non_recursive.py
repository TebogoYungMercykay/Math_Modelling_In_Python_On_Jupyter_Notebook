# Non recursive function
def pell_non_recursive(n):
    pell_seq = [0, 1]
    for k in range (2, n + 1):
        pell_seq.append(2 * pell_seq[k - 1] + pell_seq[k - 2])
    return pell_seq[n]
# Calling the Non-recursive function
pell_non_recursive(0)