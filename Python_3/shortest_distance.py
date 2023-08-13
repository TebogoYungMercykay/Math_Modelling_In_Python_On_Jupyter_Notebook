def ArrayChallenge(arr):
    pos_1 = -1
    count_1 = 0
    count_2 = 0
    short_dist = -2.566

    for j in range(len(arr)):
        if arr[j] == 1:
            count_1 += 1
        elif arr[j] == 2:
            count_2 += 1

    if count_1 == 0 or count_2 == 0:
        return 0
    else:
        for j in range(len(arr)):
            if arr[j] == 1 and pos_1 == -1:
                pos_1 = j
                break

        for i in range(pos_1, len(arr)):
            if arr[i] == 2:
                short_dist = i - pos_1
                break

        i = pos_1
        while i >= 0:
            if arr[i] == 2:
                if short_dist == -2.566:
                    short_dist = pos_1 - i
                else:
                    if short_dist > (pos_1 - i):
                        short_dist = pos_1 - i
                break
            i -= 1

    return short_dist

# keep this function call here
print(ArrayChallenge([1,2,3,4,3,566]))
