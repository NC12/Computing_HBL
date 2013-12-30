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
