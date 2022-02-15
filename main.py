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
                if not won:
                    won = check_diagonals(grid, (j, i))
                if won:
                    return won, grid.table[j][i]
    return False, 0


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


def main():
    game_grid = Grid()
    end = winner(game_grid)
    player = 1
    while not end[0]:
        play_round(game_grid, player)
        end = winner(game_grid)
        print(game_grid.table)
        player = (player % 2) + 1
    print("GG, player", end[1], "won")


if __name__ == "__main__":
    main()