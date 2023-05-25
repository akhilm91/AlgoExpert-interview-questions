def tournamentWinner(competitions, results):
    winner_map = {}
    for i in range(len(results)):
        winner = 1 - results[i]
        if competitions[i][winner] in winner_map:
            winner_map[competitions[i][winner]] = winner_map[competitions[i][winner]] + 1
        else:
            winner_map[competitions[i][winner]] = 1
    return max(winner_map, key=winner_map.get)
