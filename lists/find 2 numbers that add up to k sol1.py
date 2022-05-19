#brute force
def find_sum(lst, k):
    # iterate lst with i
    for i in range(len(lst)):
        # iterate lst with j
        for j in range(len(lst)):
            # if sum of two iterators is k
            # and i is not equal to j
            # then we have our answer
            if(lst[i]+lst[j] is k and i is not j):
                return [lst[i], lst[j]]


print(find_sum([1, 2, 3, 4], 5))