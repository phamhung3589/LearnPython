# A Naive recursive Python program to fin minimum number operations to convert str1 to str2
def edit_distance_recursive(str1, str2, m, n):
    # If first string is empty, the only option is to insert all character of first string
    if m == 0:
        return n

    # If second string is empty, the only option is to remove all character of second string
    if n == 0:
        return m

    # If the last character of two string are same, nothing much to do. Ignore last characters and get count for
    # remaining string
    if str1[m-1] == str2[n-1]:
        return edit_distance_recursive(str1, str2, m-1, n-1)

    # else consider all three case on last character of first string, recursively compute minimum cost for all three
    # operations and take minimum of three values
    return 1 + min(edit_distance_recursive(str1, str2, m, n-1),     # Insert
                   edit_distance_recursive(str1, str2, m-1, n-1),   # Replace
                   edit_distance_recursive(str1, str2, m-1, n))     # Remove


def edit_distance_dp(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    # If first string is empty, the only option is to insert all character of first string
    for i in range(n+1):
        dp[0][i] = i

    # If second string is empty, the only option is to remove all character of second string
    for i in range(m+1):
        dp[i][0] = i

    # Fill dp[][] in bottom up manner
    for i in range(1, m+1):
        for j in range(1, n+1):
            # If the last character of two string are same, nothing much to do. Ignore last characters and get count for
            # remaining string
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            # else consider all three case on last character of first string, recursively compute minimum cost for all three
            # operations and take minimum of three values
            else:
                dp[i][j] = 1 + min(dp[i][j-1],  # insert
                               dp[i-1][j-1],    # Replace
                               dp[i-1][j])      # Remove

    return dp[m][n]

if __name__ == "__main__":
    str1 = "sunday"
    str2 = "saturday"
    # min_edit = edit_distance_recursive(str1, str2, len(str1), len(str2))
    min_edit = edit_distance_dp(str1, str2)
    print("min edit distance to convert str1 to str2 is: ", min_edit)
