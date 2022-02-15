class Grid:
    def __init__(self, line = 6, column = 7):
        self.line_number = line
        self.column_number = column
        self.table = [[0 for i in range(line)] for j in range(column)]

    def space(self, column):
        for i in self.table[column]:
            if i == 0:
                return True
        return False

    def add_token(self, player, column):
        if self.space(column):
            i = 0
            while self.table[column][i] != 0:
                i += 1
            self.table[column][i] = player
        else:
            raise ValueError("Column full")


if __name__ == "__main__":
    print('import this somewhere')
