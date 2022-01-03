
def binary_search(li, item):
    left, right = 0, len(li) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if li[mid] == item:
            return mid
        if li[mid] < item:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == '__main__':
    lists = [55, 2, 71, 6, 19, 40, 39, 52, 61, 1, 90, 35, 67, 47, 25, 83]
    lists.sort()
    print(lists)
    search_item = 47

    result = binary_search(lists, search_item)
    if result:
        if result == -1:
            print(f'{search_item} item not found in list.!')
        else:
            print(f'{search_item} item found in list. Index at {result}')


""" Complexity

** Worst case time complexity ---> O(log n)
** Best case complexity       ---> O(1)
** Average case complexity    ---> O(log n)
** Space complexity           ---> O(1)

"""