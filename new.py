def largest_X_area(grid):
    rows = len(grid)
    cols = len(grid[0])

    def expand(x, y, color):
        area = 0
        while 0 <= x < rows and 0 <= y < cols and grid[x][y] == color:
            area += 1
            x += 1
            y += 1
        return area

    max_area_B = 0
    max_area_W = 0

    # Check black cells
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "B":
                # Check X shape from black cell
                area = 1 + expand(i + 1, j + 1, "B") + expand(i - 1, j + 1, "B")
                max_area_B = max(max_area_B, area)
    print(max_area_B)

    # Check white cells
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "W":
                # Check X shape from white cell
                area = 1 + expand(i + 1, j + 1, "W") + expand(i - 1, j + 1, "W")
                max_area_W = max(max_area_W, area)
    print(max_area_W)

    return max_area_W*max_area_B

# Read input
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

# Calculate and print the result
result = largest_X_area(grid)
print(result)
