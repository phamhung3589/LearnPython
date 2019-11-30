
def max_product_longest_palindrome_subsequence(s):
    max_product = 0
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for k in range(2, n+1):
        for i in range(n-k+1):
            j = i+k-1
            if s[i] == s[j] and k == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    for i in range(n-1):
        max_product = max(max_product, dp[0][i]*dp[i+1][n-1])

    return max_product

if __name__ == "__main__":
    s = "acdapmpomp"
    max_product = max_product_longest_palindrome_subsequence(s)
    print("max product of string s is: ", max_product)
