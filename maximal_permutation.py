
def max_permute(container, firstIndex, secondIndex, slides):
    set_index = set()
    len_c = len(container)
    for i in range(len(slides)):
        first = (firstIndex[i] - slides[i]%len_c + len_c)%len_c
        second = (secondIndex[i] + slides[i]%len_c)%len_c
        set_index.add(first)
        set_index.add(second)
    new_arr = [container[i] for i in set_index]
    new_arr = sorted(new_arr, reverse=True)
    new_list = sorted(list(set_index))
    for i in range(len(new_list)):
        container[new_list[i]] = new_arr[i]


if __name__ == "__main__":
    container = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    firstIndex = [0, 1, 2, 3]
    secondIndex = [1, 3, 4, 7]
    slides = [12, 13, 14, 15]
    max_permute(container, firstIndex, secondIndex, slides)
    print(container)