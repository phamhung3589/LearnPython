
def fib_memoization(n, lookup):
    if n == 0 or n == 1:
        lookup[n] = n

    if lookup[n] is None:
        lookup[n] = fib_memoization(n-1, lookup) + fib_memoization(n-2, lookup)

    return lookup[n]

def fib_tabulation(n):
    f = [0]*(n+1)
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f

if __name__ == "__main__":
    n = 34
    lookup = [None]*100
    fib_memoization(n, lookup)
    print(n, "fibonacci number is: ", lookup[:n+1])
    print(n, "fibonacci number is: ", fib_tabulation(n))