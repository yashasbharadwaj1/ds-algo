def longest_palindrome_subsequence_recursive(s, start_index,end_index):
    if start_index > end_index:
        return 0
    if start_index == end_index:
        return  1
    #case:1 elements at beginning and end are same
    if s[start_index] ==s[end_index]:
        return 2 + longest_palindrome_subsequence_recursive(s,
                                                            start_index+1,end_index-1)

   #case2 : skip one element from beginning or end
    c1 = longest_palindrome_subsequence_recursive(s, start_index + 1, end_index)
    c2 = longest_palindrome_subsequence_recursive(s, start_index, end_index - 1)
    return max(c1, c2)
def longest_palindromic_subsequence(s):
    """
    Finds the longest palindromic subsequence length
    :param s: Input string
    :return: Length of longest palindromic subsequence
    """
    return longest_palindrome_subsequence_recursive(s, 0, len(s) - 1)


# Driver code to test the above function
if __name__ == '__main__':
    print(longest_palindromic_subsequence("cddpd"))
    print(longest_palindromic_subsequence("abdbca"))
    print(longest_palindromic_subsequence("cddpd"))
    print(longest_palindromic_subsequence("pqr"))