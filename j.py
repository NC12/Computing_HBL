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

players.append(["def", 99909])
players.append(["abc", 99909])

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

def locate(elements, username, target, low, high):
    mid = (low + high) // 2
    if low == high:
        if username < elements[mid][0]:
            if low != 0:
                low -= 1
        else:
            low += 1
        return low
    elif elements[mid][1] == target:
        if username < elements[mid][0]:
            mid -= 1
        else:
            mid += 1
        return mid
    elif target < elements[mid][1]:
        return locate(elements, target, mid + 1, high)
    elif target > elements[mid][1]:
        return locate(elements, target, low, mid - 1)
    
def insert(username, score, players):
    position = locate(players, username, score, 0, len(players) - 1)
    if position == len(players):
        players.append([username, score])
    else:
        for i in range(position, len(players)):
            players[i + 1] = players[i]
        players[position] = [username, score]
    print("Insert complete!")
    
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
    pos = binary_search(players_sorted, username, 0, len(players) - 1)
    if pos == -1:
        print("User not found")
    else:
        print("Score: " + str(players_sorted[pos][1]))

def same_score(players):
    same = []
    pos = 0
    # start with 1st score
    score = players[0][1]
    while pos < len(players) - 1:
        # compare score with next score
        while score == players[pos+1][1]:
            same.append(players[pos])
            pos +=1
            # if 2nd last score and last score are the same
            if pos == len(players) - 1:
                same.append(players[pos])
        # if score not same with next score, move to the next score to compare
        score = players[pos][1]
    print(same)

def binary_search_score(elements, target, low, high):
    mid = (low + high) // 2
    if low > high:
        return -1
    elif elements[mid][1] == target:
        return mid
    elif target < elements[mid][1]:
        return binary_search(elements, target, mid + 1, high)
    elif target > elements[mid][1]:
        return binary_search(elements, target, low, mid - 1)
    
def compare(score, players):
    pos = binary_search_score(players, score, 0, len(players) - 1)
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

def generate(score, players):
    pos = binary_search_score(players, score, 0, len(players) - 1)
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
    
def menu():
    print("[1] Insert New Player")
    print("[2] Find Score by Username")
    print("[3] Generate List of Players with Same Score")
    print("[4] Compare Your Score within 5 Ranks")
    print("[5] Find 5 players above & below your rank")
    print("[0] Exit")

while True:
    menu()
    choice = input("Choose an option")
    if choice == 1:
        username = input("Enter Username: ")
        score = int(input("Enter Score: "))
        insert(username, score, players_sorted)
    if choice == 2:
        username = input("Enter Username: ")
        find_player(username, players_sorted)
    if choice == 3:
        same_score(players_sorted)
    if choice == 4:
        score = int(input("Enter Score: "))
        compare(score, players_sorted)
    if choice == 5:
        score = int(input("Enter Score: "))
        generate(score, players_sorted)
    if choice == 0:
        break
    else:
        print("Invalid choice")

