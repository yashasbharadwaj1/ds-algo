# top-down-memoization sol
memo = {}  # dictionary for Memoization


def fib(n):
    if n == 0:  # base case 1
        return 0
    if n == 1:  # base case 2
        return 1
    elif n in memo:  # Check if result for n has already been evaluated
        return memo[n]  # return the result if it is available
    else:  # otherwise recursive step
        memo[n] = fib(n - 1) + fib(n - 2)  # store the result of n in memoization dictionary
        return memo[n]  # return the value


print(fib(100))


# bottom-up-sol
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    secondlast = 0
    last = 1
    current = None
    for i in range(1, n):
        current = secondlast + last
        secondlast = last
        last = current
    return current


print(fibo(6))
