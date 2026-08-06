def find_lcs(first_seq, second_seq):
    len1 = len(first_seq)
    len2 = len(second_seq)

    table = [[0 for col in range(len2 + 1)] for row in range(len1 + 1)]

    for row in range(1, len1 + 1):
        for col in range(1, len2 + 1):
            if first_seq[row - 1] == second_seq[col - 1]:
                table[row][col] = table[row - 1][col - 1] + 1
            else:
                table[row][col] = max(table[row - 1][col], table[row][col - 1])

    row = len1
    col = len2
    result = ""

    while row > 0 and col > 0:
        if first_seq[row - 1] == second_seq[col - 1]:
            result = first_seq[row - 1] + result
            row -= 1
            col -= 1
        elif table[row - 1][col] > table[row][col - 1]:
            row -= 1
        else:
            col -= 1

    return result, table[len1][len2]

text1 = input("Enter the first string: ")
text2 = input("Enter the second string: ")

subsequence, lcs_size = find_lcs(text1, text2)

print("\nLongest Common Subsequence:", subsequence)
print("Length:", lcs_size)
# Output:
# Enter the first string: XMJYAUZ
# Enter the second string: MZJAWXU
# LCS: MJAU
# LCS Length: 4
