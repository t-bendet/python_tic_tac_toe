from tic_tac_toe.winner_or_draw import winner
from tic_tac_toe.game_Board import game_in_process
from time import sleep
from os import system


def example(dic):
    x = 'example' if dic['number of rounds'] == 0 else 'reminder'
    print(f'{x}:\n'
          'when it\'s your turn type in your move in the following syntax:\n'
          'first type in the row number  (1) then "," and then the column number (3) with no space between\n'
          'for example: 1,3 means the first row and the third column ')
    example_matrix = [
        [' ', ' ', 'X'],  # game[0]
        [' ', ' ', ' '],  # game[1]
        [' ', ' ', ' ']  # game[2]
    ]
    game_in_process(example_matrix)


def user_input(info, first_move):
    example(info)
    sleep(5)
    second_move = 'player_x' if first_move == 'player_o' else 'player_o'
    matrix = [
        [' ', ' ', ' '],  # game[0]
        [' ', ' ', ' '],  # game[1]
        [' ', ' ', ' ']  # game[2]
    ]
    while True:
        while True:
            try:
                sleep(5)
                system('cls')
                first = list(input(f"{info[first_move]['name']} turn to move({info[first_move]['char']}):"))
                if len(first) != 3:
                    print("follow the syntax")
                    example(info)
                    continue
                if int(first[0]) == 0 or int(first[2]) == 0:
                    print("column's and row's must be a number between 1-3,not zero's")
                    example(info)
                    continue
                if matrix[int(first[0]) - 1][int(first[2]) - 1] == ' ':
                    matrix[int(first[0]) - 1][int(first[2]) - 1] = f"{info[first_move]['char']}"
                    game_in_process(matrix)
                    break
                else:
                    print('this position is full')
            except IndexError:
                print("column's and row's must be a number between 1-3")
                example(info)
            except ValueError:
                print("column's and row's must be a number between 1-3")
                example(info)
        if winner(matrix):
            return winner(matrix)
        while True:
            try:
                sleep(5)
                system('cls')
                second = list(input(f"{info[second_move]['name']} turn to move({info[second_move]['char']}):"))
                if len(second) != 3:
                    print("follow the syntax")
                    example(info)
                    continue
                if int(second[0]) == 0 or int(second[2]) == 0:
                    print("column's and row's must be a number between 1-3,not zero's")
                    continue
                if matrix[int(second[0]) - 1][int(second[2]) - 1] == ' ':
                    matrix[int(second[0]) - 1][int(second[2]) - 1] = f"{info[second_move]['char']}"
                    game_in_process(matrix)
                    break
                else:
                    print('this position is full')
            except IndexError:
                print("column's and row's must be a number between 1-3")
                example(info)
            except ValueError:
                print("column's and row's must be a number between 1-3")
                example(info)
        if winner(matrix):
            return winner(matrix)
