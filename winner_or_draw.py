def is_winner_row(winner_row):
    for row in range(len(winner_row)):
        if winner_row[row].count('X') == 3:
            return 'player_x'
        elif winner_row[row].count('O') == 3:
            return 'player_o'


def is_winner_column(winner_column):
    for column in range(len(winner_column)):
        checking = []
        for row in range(len(winner_column)):
            checking.append(winner_column[row][column])
        if checking.count('X') == 3:
            return 'player_x'
        elif checking.count('O') == 3:
            return 'player_o'


def is_winner_diagonal(winner_diagonal):
    checking = []
    for i in range(len(winner_diagonal)):
        checking.append(winner_diagonal[i][i])
    if checking.count('X') == 3:
        return 'player_x'
    elif checking.count('O') == 3:
        return 'player_o'


def is_winner_diagonal_2(winner_diagonal_2):
    checking = []
    count = 2
    for i in range(len(winner_diagonal_2)):
        checking.append(winner_diagonal_2[i][count])
        count -= 1
    if checking.count('X') == 3:
        return 'player_x'
    elif checking.count('O') == 3:
        return 'player_o'


def board_full(board_matrix):
    for row in range(3):
        for col in range(3):
            if board_matrix[row][col] == ' ':
                return False
    return True


def winner(game_matrix):
    if is_winner_row(game_matrix):
        return is_winner_row(game_matrix)
    elif is_winner_column(game_matrix):
        return is_winner_column(game_matrix)
    elif is_winner_diagonal(game_matrix):
        return is_winner_diagonal(game_matrix)
    elif is_winner_diagonal_2(game_matrix):
        return is_winner_diagonal_2(game_matrix)
    elif board_full(game_matrix):
        return 'draw'


