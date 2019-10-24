# A Naive recursive python program to find length of the shortest supersequence
def scs_recursive(str1, str2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m

    if str1[m-1] == str2[n-1]:
        return 1 + scs_recursive(str1, str2, m-1, n-1)

    return 1 + min(scs_recursive(str1, str2, m-1, n), scs_recursive(str1, str2, m, n-1))

# using dynamic programming approach to solve this problem
def scs_dp(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    # Fill table in bottom up manner
    for i in range(m+1):
        for j in range(n+1):

            # Below steps follow above recurrence
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])

    # print the shortest common super sequence
    # dp[m][n] stores the length of the shortest super sequence of X and Y
    i, j, index = m, n, dp[m][n]

    # Sequence to store the shortest common super sequence
    sequence = [None for _ in range(index)]

    # Start from the bottom right corner and one by one push characters in output string
    while i > 0 and j > 0:
        # If current character in X and Y are same, then current character is part of shortest supersequence
        if str1[i-1] == str2[j-1]:
            # Put current character in result
            sequence[index-1] = str1[i-1]
            # reduce value of i, j
            i -= 1
            j -= 1

        # If current character of X and Y are different
        else:
            if dp[i-1][j] < dp[i][j-1]:
                sequence[index-1] = str1[i-1]
                i -= 1
            else:
                sequence[index-1] = str2[j-1]
                j -= 1
        index -= 1

    # If str2 reaches its end, put remaining characters of str1 in the result string
    while i > 0:
        sequence[index-1] = str1[i-1]
        i -= 1
        index -= 1

    # If str1 reaches its end, put remaining characters of str2 in the result string
    while j > 0:
        sequence[index-1] = str2[j-1]
        j -= 1
        index -= 1

    print("Shortest common super sequence is:", "".join(sequence))

    return dp[m][n]

# Using longest common subsequence to solve this challenge - scs = len(str1) + len(str2) - lcs(str1, str2)
def scs_dp_using_lcs(str1, str2):
    m, n = len(str1), len(str2)
    # declaring the array for storing the dp values
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    #Following steps build dp[m+1][n+1] in bottom up fashion. Note: L[i][j] contains length of LCS of X[0..i-1]
    # and Y[0..j-1]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # result = len(str1) + len(str2) - len(longest_common_subsequence)
    return m + n - dp[m][n]

if __name__ == "__main__":
    str1 = "AGGTAB"
    str2 = "GXTXAYB"
    print("the length of shortest common super sequence is:", scs_dp(str1, str2))