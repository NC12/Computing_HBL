def quick_sort_name(elements):
    if elements == []:
        return []
    else:
        pivot = elements[0]
        less = []
        great = []
        for item in elements[1:]:
            if item[0] < pivot[0]:
                less.append(item)
            else:
                great.append(item)
            less = quick_sort(less)
            great = quick_sort(great)
        elements = less + [pivot] + great
    return elements
players_sorted_name = quick_sort_name(players)
print(players_sorted_name)

def binary_search(elements, target, low, high):
    mid = (low + high) // 2
    if low > high:
        return -1
    elif elements[mid][0] == target:
        return mid
    elif target < elements[mid][0]:
        return binary_search(elements, target, low, mid - 1)
    elif target > elements[mid][0]:
        return binary_search(elements, target, mid + 1, high)

def find_player(username, players):
    players_sorted = quick_sort_name(players)
    pos = binary_search(players_sorted, username, 0, len(players))
    if pos == -1:
        print("User not found")
    else:
        print("Score: " + str(players_sorted[pos][1]))
