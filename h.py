def binary_search_score(elements, target, low, high):
    mid = (low + high) // 2
    if low > high:
        return -1
    elif elements[mid][1] == target:
        return mid
    elif target < elements[mid][1]:
        return binary_search(elements, target, low, mid - 1)
    elif target > elements[mid][1]:
        return binary_search(elements, target, mid + 1, high)
def generate(score, players):
    pos = binary_search_score(players, score, 0, len(players))
    less = []
    great = []
    for i in range(5):
        less.append(players[pos-i])
        great.append(players[pos+i])
    print("5 Players Above:")
    for i in range(5):
        print("Username: " + str(great[i][0]))
        print("Score: " + str(great[i][1]))
    print("Your Score: " + str(score))
    print("5 Players Below:")
    for i in range(5):
        print("Username: " + str(less[i][0]))
        print("Score: " + str(less[i][1]))
