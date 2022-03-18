def cavityMap(grid):
    grid2 = [list(x) for x in grid]

    for i in range(1, len(grid2) - 1):
        for j in range(1, len(grid2) - 1):
            if grid2[i][j] > grid2[i - 1][j] and grid2[i][j] > grid2[i + 1][j] and grid2[i][j] > grid2[i][j - 1] and grid2[i][j] > grid2[i][j + 1]:

                grid2[i][j] = "X"

    return ["".join(x) for x in grid2]


print(cavityMap(['1112', '1912', '1892', '1234']))