import math


# given points = [[2, 3], [-1, 3], [4, 5], [1, 3], [-1, 3]]
#       vertex = [2, 4]
#       k = 2
# Q: Find the k points nearest to the given vertex
def cal_distance(p1, p2):
    square = [(a-b)**2 for a, b in zip(p1, p2)]
    return math.sqrt(sum(square))


def find_num(points, vertex, points_to_return):
    distances = [[cal_distance(p, vertex), i] for i, p in enumerate(points)]
    max_v = distances[0][0]
    result = [distances[0]]
    len_result = 1
    for i in range(1, len(distances)):
        if len_result < points_to_return:
            result.append(distances[i])
            if distances[i][0] > max_v:
                max_v = distances[i][0]
                result[-1], result[0] = result[0], result[-1]
            len_result += 1

        else:
            if distances[i][0] < max_v:
                result[0] = distances[i]
                max_v = heapyfy(result)

    return [points[i] for _, i in result]


# Max heap
def heapyfy(arr):
    n = (len(arr)-2)//2
    for i in range(n+1):
        l, r = 2*i+1, 2*i+2

        if l < len(arr) and arr[i][0] < arr[l][0]:
            arr[i], arr[l] = arr[l], arr[i]

        if r < len(arr) and arr[i][0] < arr[r][0]:
            arr[i], arr[r] = arr[r], arr[i]

    return arr[0][0]


if __name__ == "__main__":
    points = [[2, 3], [-1, 3], [4, 5], [1, 3], [-1, 3]]
    vertex = [2, 4]
    points_to_return = 2
    print(find_num(points, vertex, points_to_return))
