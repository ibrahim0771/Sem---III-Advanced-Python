def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i = m
    j = n
    lcs = ""

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs = str1[i - 1] + lcs
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs, dp[m][n]

sequence1 = input("Enter the first string: ")
sequence2 = input("Enter the second string: ")

lcs, length = longest_common_subsequence(sequence1, sequence2)

print("\nLCS:", lcs)
print("LCS Length:", length)

# Output:
# Enter the first string: XMJYAUZ
# Enter the second string: MZJAWXU
# LCS: MJAU
# LCS Length: 4