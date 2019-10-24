
def preprocess(s, n, dp):

    # Substring with length = 1 is palindrome
    for i in range(n):
        dp[i][i] = True

    # k is length of substring
    for k in range(2, n+1):
        # iterate for every index with length = i
        for i in range(n-k+1):
            j = i+k-1
            # Only check when s[i] == s[j] and assign dp[i][j] to True if substring[i, j] is palindrome
            if s[i] == s[j] and k == 2:
                dp[i][j] = True
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]

def count_pair(s):
    result = 0

    # Get length of s
    n = len(s)

    # Create the dp table initially
    dp = [[False for _ in range(n)] for _ in range(n)]
    preprocess(s, n, dp)

    # Declare of the left array - left[i] count all palindrome with decrease length from index 0, 1, 2, ... -> i
    left = [0 for _ in range(n)]
    # Declare the right array - right[i] count all palindrome with decrease length from index n-1, n-2,... -> i
    right = [0 for _ in range(n)]

    # Count the number of palindrome pairs to the left
    left[0] = 1
    for i in range(1, n):
        for j in range(i+1):
            if dp[j][i] == True:
                left[i] += 1

    # Count the number of palindrome pairs to the right
    right[n-1] = 1
    for i in range(n-2, -1, -1):
        right[i] = right[i+1]
        for j in range(n-1, i-1, -1):
            if dp[i][j] == True:
                right[i] += 1

    # Count the number of pairs
    for i in range(n-1):
        result += left[i] * right[i+1]

    return result

if __name__ == "__main__":
    s = "abacaba"
    result = count_pair(s)
    print("count of no overlapping palindrome substring is: ", result)