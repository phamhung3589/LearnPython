# using recursive approach
# assume s = "hunghuy", if s[0] == s[n] (h and y) lps = 2 + s[1:n-1]
#                       if s[0] != s[n], lps = max(lps(s[1:n]), lps(s[0:n-1]))
def lps_recursive(s, l, r):
    if l > r:
        return 0

    # if l == r => len(s) = 1 => lps = 1
    if l == r:
        return 1

    if s[l] == s[r]:
        return 2 + lps_recursive(s, l+1, r-1)

    else:
        return max(lps_recursive(s, l+1, r), lps_recursive(s, l, r-1))


# using dynamic programming approach
def lps_dp(s):
    # len of s
    n = len(s)
    # Create a table to store results of subproblems
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # with string have length = 1 then lps = 1
    for i in range(n):
        dp[i][i] = 1

    # iterate throw s from j to i: with i running from 1-n, j running from i-1_0
    for i in range(1, n):
        for j in range(i-1, -1, -1):

            # if length of s = 2 and have same character => lps = 2
            if s[j] == s[i] and i-j==1:
                dp[j][i] = 2

            # if the first and last character are the same then lps = 2 + s[1:n]
            elif s[j] == s[i]:
                dp[j][i] = 2 + dp[j+1][i-1]

            else:
                dp[j][i] = max(dp[j+1][i], dp[j][i-1])

    return dp[0][n-1]


def lps(s):
    n = len(s)
    # Create a table to store results of subproblems
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # k is length of substring
    for k in range(2, n+1):
        for i in range(n-k+1):
            j = i+k-1
            if s[i] == s[j] and k == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][n-1]

# Returns the length of the longest palindromic subsequence in str with O(n) in space
def lps_On_space(s):
    n = len(s)
    # a[i] is going to store length of longest palindromic subsequence of substring s[0..i]
    a = [0 for _ in range(n)]

    # Pick starting point
    for i in range(n-1, -1, -1):
        back_up = 0

        # Pick ending points and see if s[i] increases length of longest common subsequence ending with s[j].
        for j in range(i, n):

            # similar to 2D array L[i][j] == 1 i.e., handling substrings of length one.
            if i == j:
                a[j] = 1

            # Similar to 2D array L[i][j] = L[i+1][j-1]+2 i.e., handling case when corner characters are same.
            elif s[i] == s[j]:
                tmp = a[j]
                a[j] = back_up + 2
                back_up = tmp

            # similar to 2D array L[i][j] = max(L[i][j-1], a[i+1][j])
            else:
                back_up = a[j]
                a[j] = max(a[j-1], a[j])

    return a[n-1]

def print_longest_palindrome_subsequence(X, Y):
    n = len(X)
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(n):
        for j in range(n):
            if X[i] == Y[j]:
                dp[i+1][j+1] = 1 + dp[i][j]
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    i, j = n, n
    sequence = ""
    while( i > 0 and j > 0):
        if X[i-1] == Y[j-1]:
            sequence = X[i-1] + sequence
            i, j = i-1, j-1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                i = i-1
            else:
                j -= 1
    return sequence

if __name__ == "__main__":
    s = "GEEKSFORGEEKS"
    max_palindrome_recursive = lps_recursive(s, 0, len(s)-1)
    # max_palindrome = lps(s)
    max_palindrome = lps_On_space(s)
    print("The length of the longest palindrome subsequence using recursive approach is : ", max_palindrome_recursive)
    print("The length of the longest palindrome subsequence: ", max_palindrome)
    print("the longest palindorme is: ", print_longest_palindrome_subsequence(s, s[::-1]))
