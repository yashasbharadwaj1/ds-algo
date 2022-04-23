def can_partition_recursive(set,set_length,sum,current_index):
    if sum ==0:
        return True
    if set_length ==0 or current_index >=set_length:
        return False
    # recursive call after choosing the number at the current_index
    # if the number at current_index exceeds the sum, we shouldn't process this
    if set[current_index] <=sum:
        if can_partition_recursive(set,
                                   set_length,sum-set[current_index],
                                   current_index+1):
            return True
    return can_partition_recursive(set,set_length,sum,current_index+1)


def can_partition(set):
    set_length =len(set)
    sum=0
    for i in range(set_length):
        sum +=set[i]
    if sum %2 !=0:
        return False
    return can_partition_recursive(set,set_length,sum//2,0)

if __name__ == '__main__':
    set1 = [1, 2, 3, 4]
    print(can_partition(set1))

    set2 = [1, 1, 3, 4, 7]
    print(can_partition(set2))

    set3 = [2, 3, 4, 6]
    print(can_partition(set3))