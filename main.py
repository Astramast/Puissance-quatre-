from grid import Grid


def check_ldiagonal(grid, pos):
    count = 1
    while grid.table[pos[0]][pos[1]] == grid.table[pos[0] - count][pos[1] - count] and count < 4:
        count += 1
    if count == 4:
        return True
    else:
        return False


def check_rdiagonal(grid, pos):
    count = 1
    while grid.table[pos[0]][pos[1]] == grid.table[pos[0] + count][pos[1] + count] and count < 4:
        count += 1
    if count == 4:
        return True
    else:
        return False


def check_diagonals(grid, pos):
    left = right = False
    if pos[0] >= 4:
        left = check_ldiagonal(grid, pos)
    if pos[0] <= grid.column_number - 4:
        right = check_rdiagonal(grid, pos)
    return left or right


def check_line(grid, pos):
    count = 1
    while grid.table[pos[0]][pos[1]] == grid.table[pos[0]+count][pos[1]] and count < 4:
        count += 1
    if count == 4:
        return True
    else:
        return False


def check_stack(grid, pos):
    count = 1
    while grid.table[pos[0]][pos[1]] == grid.table[pos[0]][pos[1]+count] and count < 4:
        count += 1
    if count == 4:
        return True
    else:
        return False


def winner(grid):
    for i in range(grid.line_number):
        for j in range(grid.column_number):
            



def main():
    game_grid = Grid()


if __name__ == "__main__":
    main()