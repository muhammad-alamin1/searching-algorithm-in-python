def linear_search(li, item):
    n = len(li)

    i = 0
    while i < n:
        if li[i] == item:
            return i
        i += 1

    i = -1
    return i


""" Different way :

def linear_search(list, item):
    n = len(list)
    
    for i in range(n):
        if list[i] == item:
            return i
    return -1
    
"""

if __name__ == '__main__':
    lists = [2225, 4, 2, 34, 64, 1, 43, 5, 644, 23, 2247, 6, 1243]
    search_item = 2247
    result = linear_search(lists, search_item)
    print(f'{search_item} item index at {result} in lists array.')


""" Complexity 

** Worst time complexity   ---> O(n)
** Best case complexity    ---> O(1)
** Average Case complexity ---> O(n)
** Space complexity        ---> O(1)

"""