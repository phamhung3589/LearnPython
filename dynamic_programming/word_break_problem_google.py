# Naive solution for break the word into sub-word using recursive
def word_break_recursive(dict, freq, word):
    if word == "":
        return True
    check = False
    for f in freq:
        if word[:f] in dict:
            check = check or word_break_recursive(dict, freq, word[f:])
        if check: return check

    return check

# Using dynamic programming to solve this problem
# Returns true if string can be segmented into space separated words, otherwise returns false
def word_break_dp(dict, word):
    n = len(word)
    if n == 0:
        return True

    # Create the DP table to store results of subroblems. The value dp[i]
    # will be true if str[0..i-1] can be segmented into dictionary words, otherwise false
    dp = [False for _ in range(n+1)]
    for i in range(1, n+1):

        # if dp[i] is false, then check if current prefix can make it true.Current prefix is "str.substr(0, i)"
        if dp[i] == False and word[:i] in dict:
            dp[i] = True

        # dp[i] is true, then check for all substrings starting from (i+1)th character and store their results.
        if dp[i]:

            # If we reach the last prefix
            if i == n:
                return True

            for j in range(i+1, n+1):
                # Update wb[j] if it is false and can be updated Note the parameter passed to dictionaryContains() is
                # substring starting from index 'i' and length 'j-i'
                if dp[j] == False and word[i:j] in dict:
                    dp[j] = True

                    # If we reach the last character
                    if j == n:
                        return True

    # If we have tried all prefixes and none of them worked
    return False

# Using index array to store index of last character can be partitioned
def word_break_dp_optimize(dictionary, word):
    n = len(word)

    if n == 0:
        return True

    # Create the DP table to store results of subroblems. The value dp[i] will be true if str[0..i] can be
    # segmented into dictionary words, otherwise false
    dp = [False for _ in range(n+1)]

    # matched_index array represents the indexes for which dp[i] is true. Initially only -1 element is present in this array
    index = [-1]

    for i in range(1, n+1):
        size = len(index)

        # Flag value which tells that a substring matches with given words or not.
        check = False

        # Check all the substring from the indexes matched earlier. If any of that substring matches than make flag
        # value = 1
        for j in range(size):
            # check substring starting from index[j] + 1 and of stop with i
            if word[index[j]+1:i] in dictionary:
                check = True
                break

        # If substring matches than do dp[i] = 1 and push that index in matched_index array.
        if check == True:
            dp[i] = True
            index.append(i-1)

    return dp[n]


if __name__ == "__main__":
    dictionary = ["mobile","samsung","sam","sung", "man","mango","icecream","and","go","i","like","ice","cream"]
    freq = set()
    for word in dictionary:
        freq.add(len(word))
    freq = sorted(list(freq))
    words = ["ilikesamsung", "iiiiiiii", "", "ilikelikeimangoiii", "samsungandmango", "samsungandmangok"]
    for word in words:
        print("This word can be break into sub word using dp approach:", word_break_dp(dictionary, word))
        print("This word can be break into sub word using dp optimize approach:", word_break_dp_optimize(dictionary, word))

