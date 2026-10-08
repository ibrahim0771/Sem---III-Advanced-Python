n = int(input("Enter the number of houses: "))
houses = list(map(int, input("Enter the amount in each house: ").split()))

dp = [0] * (n + 1)

if n >= 1:
    dp[1] = houses[0]

for i in range(2, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + houses[i - 1])

print("Maximum possible amount:", dp[n])

# Output
# Enter the number of houses: 5
# Enter the amount in each house: 100 200 300 400 500
# Maximum possible amount: 900