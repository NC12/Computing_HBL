def same_score(players):
    same = []
    occurrence = 0
    for i in range(len(players) - 1):
        score = players[i][1]
        if score == players[i+1][1] and occurrence == 0:
            same.append(players[i])
            same.append(players[i+1])
            occurrence = 1
        elif score == players[i+1][1] and occurrence == 1:
            same.append(players[i+1])
        else:
            occurence = 0
    print(same)

#same_score(players)
