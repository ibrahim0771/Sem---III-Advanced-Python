a = input("Enter the first string: ")
b = input("Enter the second string: ")

m = len(a)
n = len(b)
dp = [[0] * (n + 1) for _ in range(m + 1)]
maximum = 0

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            maximum = max(maximum, dp[i][j])

print("Length of the longest common substring:", maximum)

# output
# Enter the first string: ABCDGH
# Enter the second string: ACDGHR
# Length of the longest common substring: 4