#g
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
    rankup = pos
    rankdown = pos
    less = []
    great = []
    for i in range(5):
        #go forward/backward from position of player, store the first score of the rank above/below
        rankup += 1
        rankdown -= 1
        great.append(players[rankup])
        less.append(players[rankdown])
        #keep going forward/backward from position of player and store the rest of the players in that rank
        while players[rankup][1] == players[rankup+1][1]:
            rankup += 1
            great.append(players[rankup])
        while players[rankdown][1] == players[rankdown-1][1]:
            rankdown -= 1
            less.append(players[rankdown])
    print("5 Ranks Above:")
    for i in range(5):
        print("Username: " + str(great[i][0]))
        print("Score: " + str(great[i][1]))
    print("Your Score: " + str(score))
    print("5 Ranks Below:")
    for i in range(5):
        print("Username: " + str(less[i][0]))
        print("Score: " + str(less[i][1]))
