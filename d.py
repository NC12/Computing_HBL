#(d)
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
