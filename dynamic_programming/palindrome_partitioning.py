# Returns the minimum number of cuts needed to partition a string such that every part is a palindrome


# using recursive approach
def palindrome_partition_recursive(s):
    # Base case
    if s == s[::-1]:
        return 0

    # initial min_cutting og substring s
    min_cutting = float("inf")

    # For each position to cutting recursive with result = 1 + palindrome(s[:i]) + palindrome(s[i:])
    for i in range(1, len(s)):
        result = 1 + palindrome_partition_recursive(s[:i]) + palindrome_partition_recursive(s[i:])
        # get min over all result
        min_cutting = min(result, min_cutting)

    return min_cutting


# using dp approach
def palindrome_partition_dp(s):
    # Get the length of the string
    n = len(s)

    # dp[i][j] = minimum number of cuts needed for palindrome
    dp = [[float("inf") for _ in range(n)] for _ in range(n)]

    # Initial value for dp[i][i]
    for i in range(n):
        dp[i][i] = 0

    # Run i from 1 to n-1
    for i in range(1, n):
        # with i, looping j from i-1 to 0
        for j in range(i-1, -1, -1):
            # Check if s[i:j+1] is palindrome or not. If yes dp[j][i] = 0
            new_str = s[j:i+1]
            if new_str == new_str[::-1]:
                dp[j][i] = 0
            else:
                # dp[j][i] = Min { dp[j][k] + 1 + dp[k+1][i] } where k varies from j to i-1
                for k in range(j, i):
                    dp[j][i] = min(dp[j][i], 1 + dp[j][k] + dp[k+1][i])

    return dp[0][n-1]


# Returns the minimum number of cuts needed to partition a string such that every part is a palindrome
def palindrome_partition_optimize(s):
    # Get the length of the string
    n = len(s)

    # Create two arrays to build the solution in bottom up manner
    # dp[i] = Minimum number of cuts needed for palindrome partitioning of substring str[0..i]
    # P[i][j] = true if substring str[i..j] is palindrome, else false - Note that dp[i] is 0 if P[0][i] is true
    dp = [float("inf") for _ in range(n)]
    check = [[False for _ in range(n)] for _ in range(n)]

    # Every substring of length 1 is a palindrome
    for i in range(n):
        check[i][i] = True

    # Build the solution in bottom up manner by considering all substrings from 1 to n-1
    for i in range(1, n):
        # For each i, looping from i-1 to 0
        for j in range(i-1, -1, -1):
            # if len of substring equal to 2, we just need to compare 2 characters,
            # else to check 2 corner character and value of dp[j+1][i-1]
            if i-j == 1 and s[i] == s[j]:
                check[j][i] = True
            else:
                check[j][i] = s[j] == s[i] and check[j+1][i-1]

    # Running for dp
    for i in range(n):
        # if substring(0, i) is palindrome => dp[i] = 0, else, loop j from 0 to i-1,
        # if substring(j+1, i) is palindrome then c[i] = min(c[i], 1 + c[j])
        if check[0][i]:
            dp[i] = 0
        else:
            for j in range(i):
                if check[j+1][i]:
                    dp[i] = min(dp[i], 1 + dp[j])

    # Return the min cut value for complete string. i.e., str[0..n-1]
    return dp[n-1]


if __name__ == "__main__":
    s = "ababbbabbababa"
    result_recursive = palindrome_partition_recursive(s)
    result_dp = palindrome_partition_dp(s)
    result_optimize = palindrome_partition_optimize(s)
    print("minimum cutting of string to all substring is palindrome using recursive approach is: ", result_recursive)
    print("minimum cutting of string to all substring is palindrome using dp approach is: ", result_dp)
    print("minimum cutting of string to all substring is palindrome using optimize approach is: ", result_optimize)
