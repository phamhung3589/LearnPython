# Python program to find nth magic number: a number which can be expressed as a power of 5 or sum of unique powers of 5
# Ex: 5, 25, 30(5 + 25), 125, 130(125 + 5), ….
# magic numbers can be represented as 001, 010, 011, 100, 101, 110

def nth_magic_number(n):
    p = 1
    result = 0

    # Go through every bit of n
    while n:
        p = p*5

        # If last bit of n is set
        if n & 1:
            result += p

        # proceed to next bit ir b = n//2
        n = n>>1

    return result


if __name__ == "__main__":
    n = 5
    print(nth_magic_number(n))
