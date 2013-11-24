import random

players = []
for i in range(5000):
    username_length = random.randint(0, 9)
    alpha1 = chr(random.randint(65, 90))
    upper1 = random.randint(0, 1)
    if upper1 == 1:
        alpha1 = alpha1.upper()
    username = alpha1
    for i in range(username_length):
        char = random.randint(0, 35)
        if char > 9:
            if char % 2 == 0:
                char = chr(char + 55)
            else:
                char = chr(char + 87)
        username += str(char)
    score = random.randint(0,99999)
    players.append([username, score])

#players.append(["def", 99909])
#players.append(["abc", 99909])


def quick_sort(elements):
    if elements == []:
        return []
    else:
        pivot = elements[0]
        less = []
        great = []
        for item in elements[1:]:
            if item[1] > pivot[1]:
                great.append(item)
            elif item[1] < pivot[1]:
                less.append(item)
            else: #if score is equal
                if item[0] > pivot[0]:
                    less.append(item)
                else:
                    great.append(item)
            less = quick_sort(less)
            great = quick_sort(great)
        elements = great + [pivot] + less
    return elements
        
players_sorted = quick_sort(players)
print(players_sorted)
