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
            if grid.table[j][i] != 0:
                won = False
                if i < grid.line_number - 4:
                    won = check_stack(grid, (j, i))
                if not won and j < grid.column_number - 4:
                    won = check_line(grid, (j, i))
                if not won and i < grid.line_number - 4:
                    won = check_diagonals(grid, (j, i))
                if won:
                    return won, grid.table[j][i]
    flag = True
    for i in range(grid.column_number):
        if flag and grid.space(i):
            flag = False
    return (True, 0) if flag else (False, 0)


def player_input(grid):
    flag = True
    while flag:
        try:
            choice = input("Enter column choice : ")
            choice = int(choice)
            flag = False
        except ValueError:
            print("Enter an integer")
        if not flag:
            flag = 0 <= choice < grid.column_number
            flag = not flag
    return choice


def play_round(grid, player):
    flag = True
    while flag:
        choice = player_input(grid)
        try:
            grid.add_token(player, choice)
            flag = False
        except ValueError:
            print("This column is full !")


def stamp_grid(grid):
    for i in range(grid.line_number - 1, -1, -1):
        for j in range(grid.column_number):
            if grid.table[j][i] == 0:
                k = " "
            elif grid.table[j][i] == 1:
                k = "O"
            else:
                k = "X"
            print("|", k, end=' ')
        print("|")
    print("  0   1   2   3   4   5   6")


def main():
    game_grid = Grid()
    end = winner(game_grid)
    player = 1
    stamp_grid(game_grid)
    while not end[0]:
        play_round(game_grid, player)
        end = winner(game_grid)
        stamp_grid(game_grid)
        player = (player % 2) + 1
        print(end)
    if end[0] and end[1] == 0:
        print("Draw, you really boring players. =-= I reset the game for you.")
        main()
    else:
        print("GG, player", end[1], "won")


if __name__ == "__main__":
    main()