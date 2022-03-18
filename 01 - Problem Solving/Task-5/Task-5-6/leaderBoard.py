def climbingLeaderboard(ranked, player):
    ranked = list(set(ranked))
    ranked.sort()
    n = len(ranked)
    i = 0
    result = []

    for allScore in player:
        while i < n and ranked[i] <= allScore:
            i += 1

        result.append(n - i + 1)

    return result