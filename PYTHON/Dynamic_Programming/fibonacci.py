# Example of memoization
# Those who cannot remember the past are condemned to repeat it

# 1, 1, 2, 3, 5, 8, ...

def fib(n, memo):
    if memo[n] != null:
        return memo[n]
    if n == 1 or n == 2
        result = 1
    else:
        result = fib(n-1,memo) + fib(n-2, memo)
    memo[n] = result
    return result

# bottom up approach builds array
# no recursive calls on call stack

def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]
