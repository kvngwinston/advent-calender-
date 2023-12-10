def neighbours(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])

    r_min = max(0, r - 1)
    r_max = min(rows, r + 2)
    c_min = max(0, c - 1)
    c_max = min(cols, c + 2)

    vals = [grid[i][j] for i in range(r_min, r_max) for j in range(c_min, c_max) if (i, j) != (r, c)]
    return vals

def main():
    data = open('/Users/winstonewoof/Desktop/Desktop - MacBook Air/my school stuff/fourth year f sem/comp 371/input (2).txt').read().splitlines()
    grid = [list(line) for line in data]

    ans = 0
    num_str = ""
    symbol = False

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y].isdigit():
                num_str += grid[x][y]
                # Test if symbol nearby
                adj = neighbours(grid, x, y)
                if any(a in "!@#$%^&*()-+=/" for a in adj):
                    symbol = True
            elif num_str:
                if symbol:
                    ans += int(num_str)
                    symbol = False
                num_str = ""

    print(ans)

if __name__ == "__main__":
    main()

    
