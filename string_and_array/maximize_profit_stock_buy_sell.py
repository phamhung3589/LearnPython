def max_profit(arr):
    n = len(arr)
    max_tmp = 0
    max_profit = 0
    for i in range(n-1, -1, -1):
        max_tmp = max(max_tmp, arr[i])
        max_profit += max_tmp - arr[i]
        print(max_tmp, arr[i])

    return max_profit


if __name__ == "__main__":
    arr = [100, 180, 260, 310, 40, 535, 695]
    profit = max_profit(arr)
    print("max profit of stock by buying and selling is: ", profit)
