def fib_memo(n, memo={}):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_tab(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Driver Code
n = int(input("Enter the value of n: "))

print("Using Memoization :", fib_memo(n))
print("Using Tabulation  :", fib_tab(n))