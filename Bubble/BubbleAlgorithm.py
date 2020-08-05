
def bubble_sort(list_to_sort):

    swap_flag = 1

    while swap_flag >= 1:
        swap_flag = 0
        x = 0
        for x in range(len(list_to_sort)-1):
            if list_to_sort[x] > list_to_sort[x+1]:
                temp = list_to_sort[x]
                list_to_sort[x] = list_to_sort[x+1]
                list_to_sort[x+1] = temp
                swap_flag += 1  # checking if the swap happened

    return list_to_sort


if __name__ == '__main__':
    example_list = [6, 4, 5, 0, 9, 1, 3, 7, 2]

    bubble_sort(example_list)

    print(example_list)