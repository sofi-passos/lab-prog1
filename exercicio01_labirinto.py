def resolver_labirinto(n, m, k, maze, tunnels):
    from collections import defaultdict

    tunnel_map = {}
    for i1, j1, i2, j2 in tunnels:
        tunnel_map[(i1, j1)] = (i2, j2)
        tunnel_map[(i2, j2)] = (i1, j1)

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'A':
                start = (i, j)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        cell = maze[i][j]
        if cell == '*':
            return 0.0
        if cell == '%':
            return 1.0
        if (i, j) in tunnel_map:
            i, j = tunnel_map[(i, j)]
            cell = maze[i][j]
            if cell == '*':
                return 0.0
            if cell == '%':
                return 1.0

        moves = []
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] != '#':
                moves.append((ni, nj))

        if not moves:
            return 0.0

        prob = sum(dfs(x, y) for x, y in moves) / len(moves)
        memo[(i, j)] = prob
        return prob
