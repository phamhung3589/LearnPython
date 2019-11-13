# Python 3 program to swap even and odd bits of a given number
# Function for swapping even and odd bits
def swap_bit(n):
    # Get all even bits of x
    even_bit = n & 0xAAAAAAAA

    # Get all odd bits of x
    odd_bit = n & 0x55555555

    # Right shift even bits
    even_bit = even_bit >> 1

    # Left shift odd bits
    odd_bit = odd_bit << 1

    # Combine even and odd bits
    return even_bit | odd_bit


if __name__ == "__main__":
    n = 23
    print("swap odd and even bit of {:d} is: {:d}".format(n, swap_bit(n)))
