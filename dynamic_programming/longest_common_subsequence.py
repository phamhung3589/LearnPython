
# A Naive recursive Python implementation of LCS problem
def lcs_recursive(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs_recursive(X, Y, m-1, n-1)
    else:
        return max(lcs_recursive(X, Y, m-1, n), lcs_recursive(X, Y, m, n-1))

# Optimize solution using dynamic programming
def lcs_dp(X, Y):
    # find the length of the strings
    m, n = len(X), len(Y)

    # declaring the array for storing the dp values
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    #Following steps build dp[m+1][n+1] in bottom up fashion. Note: L[i][j] contains length of LCS of X[0..i-1]
    # and Y[0..j-1]
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                dp[i+1][j+1] = 1 + dp[i][j]
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    ### printing the longest common subsequence

    # Start from the right-most-bottom-most corner and one by one store characters in lcs[]
    i, j = m, n
    # final sequence
    sequence = ""
    while(i > 0 and j > 0):
        # If current character in X[] and Y are same, then current character is part of LCS
        if X[i-1] == Y[j-1]:
            sequence = X[i-1] + sequence
            i = i-1
            j = j-1
        # If not same, then find the larger of two and go in the direction of larger value
        else:
            if dp[i-1][j] > dp[i][j-1]:
                i = i-1
            else:
                j = j-1
    print("the longest common subsequence is: ", sequence)

    # dp[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return dp[m][n]

if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    m, n = len(X), len(Y)
    # print("longest common subsequence of X and Y is: ", lcs_recursive(X, Y, m, n))
    print("the length of the longest common subsequence of X and Y is: ", lcs_dp(X, Y))
