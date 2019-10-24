
def get_Z_array(s, n, Z):
    left, right, k = 0, 0, 0
    # [L, R] make a window which matches with prefix of s
    for i in range(n):
        # if i>R nothing matches so we will calculate Z[i] using naive way.
        if i > right:
            left, right = i, i
            # R-L = 0 in starting, so it will start checking from 0'th index. For example, for "ababab" and i = 1,
            # the value of R remains 0 and Z[i] becomes 0. For string "aaaaaa" and i = 1, Z[i] and R become 5
            while right < n and s[right-left] == s[right]:
                right += 1
            Z[i] = right - left
            right -= 1
        else:
            # k = i-L so k corresponds to number which matches in [L, R] interval.
            k = i - left
            # if Z[k] is less than remaining interval then Z[i] will be equal to Z[k].
            # For example, str = "ababab", i = 3, R = 5 and L = 2
            if Z[k] < right - i + 1:
                Z[i] = Z[k]
            else:
                left = i
                while right < n and s[right - left] == s[right]:
                    right += 1
                Z[i] = right - left
                right -= 1

def sum_similarity(s):
    n = len(s)
    Z = [0 for _ in range(n)]
    # Compute the Z-array for the given string
    get_Z_array(s, n, Z)
    # summation of the Z-values
    return n + sum(Z)

if __name__ == "__main__":
    s = "aaabaab"
    result = sum_similarity(s)
    print(result)
