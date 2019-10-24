from collections import defaultdict

def subset(arr, s):
    # Using defaultdict to increase value of each element in arr and don't need to check the exist of element in dict
    hashtable = defaultdict(int)
    result = 0
    for ele in arr:
        if (s - ele) in hashtable and hashtable[s-ele] > 0:
            result += 1
            hashtable[s-ele] -= 1
        else:
            hashtable[ele] += 1

    return result


if __name__ == "__main__":
    arr = [3, 34, 4 ,12, 5, 2, 7, 1, 8]
    s = 9
    print("number of pairs in arr with sum =", s, "is:", subset(arr, s))