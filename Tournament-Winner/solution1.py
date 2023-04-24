def tournamentWinner(competitions, results):
    # Write your code here.
    points_map = {}
    for i in range(len(results)):
        #i = 0, 1, 2
        if competitions[i][1-results[i]] in points_map:
            points_map[competitions[i][1-results[i]]] = points_map[competitions[i][1-results[i]]]+3
        else:
            points_map[competitions[i][1-results[i]]] = 3
    return max(points_map, key=points_map.get)