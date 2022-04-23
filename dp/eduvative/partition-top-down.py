def can_partition_recursive(lookup_table, set, set_length, sum, current_index):
    """
    Checks if two sub-lists has equal sum or not
    :param lookup_table: Lookup Table
    :param set: Integer list having positive numbers only
    :param set_length: length of the list
    :param sum: stores sum of the sub-list
    :param current_index: index of the sub-list
    :return: returns True if two sub-lists have equal sum, otherwise False
    """

    # base check
    if sum == 0:
        return True
    if set_length == 0 or current_index >= set_length:
        return False

    # if we have not already processed a similar problem
    if lookup_table[current_index][sum] == -1:
        # recursive call after choosing the number at the current_index
        # if the number at current_index exceeds the sum, we shouldn't process this
        if set[current_index] <= sum:
            if can_partition_recursive(lookup_table, set, set_length, sum - set[current_index], current_index + 1):
                lookup_table[current_index][sum] = True
                return True

        # recursive call after excluding the number at the current_index
        lookup_table[current_index][sum] = can_partition_recursive(lookup_table, set, set_length, sum,
                                                                   current_index + 1)

    return lookup_table[current_index][sum]


def can_partition(set):
    """
    Checks if two sub-lists has equal sum or not
    :param set: Integer list having positive numbers only
    :return: returns True if two sub-lists have equal sum, otherwise False
    """

    sum = 0
    set_length = len(set)

    for i in range(set_length):
        sum += set[i]

    # if 'sum' is a an odd number, we can't have two subsets with equal sum
    if sum % 2 != 0:
        return False

    lookup_table = [[-1 for x in range(sum // 2 + 1)] for x in range(set_length)]

    return can_partition_recursive(lookup_table, set, set_length, sum // 2, 0)


# Driver code to test the above function
if __name__ == '__main__':
    set1 = [1, 2, 3, 4]
    print(can_partition(set1))

    set2 = [1, 1, 3, 4, 7]
    print(can_partition(set2))

    set3 = [2, 3, 4, 6]
    print(can_partition(set3))
