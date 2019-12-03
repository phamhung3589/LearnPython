from collections import defaultdict


# a program to check if all words in dictionary can create a sequence with 2 nodes next together have only 1 different character
def check_node(arr):
    print(arr)
    n = len(arr)
    adj = defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            if char_diff(arr[i], arr[j]) == 1:
                adj[arr[j]].append(arr[i])
                adj[arr[i]].append(arr[j])
        if arr[i] not in adj:
            adj[arr[i]] = []
    return adj


def char_diff(str1, str2):
    n = len(str1)
    i, j = 0, 0
    check = 0
    while i < n and j < n and check < 2:
        if str1[i] != str2[j]:
            check += 1
        i += 1
        j += 1

    return check


def bfs(adj):
    n = len(adj)
    visited = {}
    for key in adj:
        visited[key] = False
    q = []
    keys = list(adj.keys())

    q.append(keys[0])
    visited[keys[0]] = True

    while len(q) > 0:
        u = q.pop(0)

        for v in adj.get(u):
            if visited[v] is False:
                visited[v] = True
                q.append(v)

    for key in visited:
        if visited[key] is False:
            return False

    return True


if __name__ == "__main__":
    arr = ["dog", "hat", "dig", "dot", "fat", "hot", "fet", "amg"]
    adj = check_node(arr)
    print(adj)
    check = bfs(adj)
    print("this dict can be a sequence with only 1 different character: ", check)
