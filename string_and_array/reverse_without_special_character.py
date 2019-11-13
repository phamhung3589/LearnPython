# Python program to reverse a string with special characters

# Returns true if x is an aplhabatic character, false otherwise
def reverse_without_special_cha(s):
    s = list(s)

    # Initialize left and right pointers
    l = 0
    r = len(s)-1

    # Traverse s from both ends until 'l' and 'r'
    while l < r:
        # Ignore special characters of the left side
        if not s[l].isalpha():
            l += 1

        # Ignore special characters of the right side
        elif not s[r].isalpha():
            r -= 1

        # Both s[l] and s[r] are not special
        else:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    return "".join(s)


if __name__ == "__main__":
    s = "a!!!b.c.d,e'f,ghi"
    print("before reverse: ", s)

    s = reverse_without_special_cha(s)

    print("After reverse: ", s)