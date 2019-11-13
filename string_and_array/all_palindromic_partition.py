import copy


# Function to print all possible palindromic partitions of str. It mainly creates vectors and calls all_palindrome()
def all_palindrome(s):
    # To Store all palindromic partitions
    result = []

    # To store current palindromic partition
    curr = []
    n = len(s)

    # Using dp to check all substring is palindrome or not of string s
    dp = check_palindrome(s)

    # Call recursive function to generate all partiions and store in allPart
    get_all_palindrome_partitions(s, 0, n, result, curr, dp)

    # Print all partitions generated by above call
    for partition in result:
        print(partition)


# Using dp approach to check all substring of s is palindrome or not
def check_palindrome(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if s[i] == s[j] and i - j == 1:
                dp[j][i] = True
            elif s[i] == s[j]:
                dp[j][i] = dp[j+1][i-1]

    return dp


# Recursive function to find all palindromic partitions of input[start..n-1] allPart -->result save all partitions.
# Every partition inside it stores a partition currPart --> A curr array to store current partition
def get_all_palindrome_partitions(s, start, end, result, curr, dp):
    # If 'start' has reached len
    if start == end:
        result.append(copy.copy(curr))
        return

    # Pick all possible ending points for substrings
    for i in range(start, end):

        # If substring str[start..i] is palindrome
        if dp[start][i]:

            # Add the substring to result
            curr.append(s[start:i+1])

            # Recur for remaining remaining substring
            get_all_palindrome_partitions(s, i+1, end, result, curr, dp)

            # Remove substring str[start..i] from current partition
            curr.pop()


if __name__ == "__main__":
    s = "nitin"
    all_palindrome(s)