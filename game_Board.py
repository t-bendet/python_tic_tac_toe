import random
from time import sleep
from os import system


def game_board(board_size):
    for index in range(board_size):
        print(" ---" * board_size)
        print("|   " * board_size + "|")
    print(" ---" * board_size)


def game_in_process(matrix):
    for index in range(3):
        print(" ---" * 3)
        x, y, z = matrix[index][0], matrix[index][1], matrix[index][2]
        print(f'| {x} | {y} | {z} | ')
    print(" ---" * 3)


def welcome():
    game_board(3)
    print('welcome to tic tac toe\n'
          'a great way to practice your cognitive abilities(if your 6-10 years old.....)\n'
          'and an excellent way for me to practice my coding\n'
          'brought to you by.....\n'
          'PYTHON...cause anybody can code....\n')
    sleep(4)
    system('cls')
    name_1 = input('first player!! come on up!!\n'
                   'and your name is....?\n')
    system('cls')
    print(f"applause for {name_1}, {name_1} you'r going to play with X\n")
    sleep(4)
    system('cls')
    name_2 = input('player number 2!! come on down!!\n'
                   'and what your name might be....?\n')
    system('cls')
    print(f"yah yah yah...{name_2}...great\n"
          f"that's all the excitement i got for now\n"
          f"{name_2} your playing O")
    sleep(4)
    system('cls')
    return name_1, name_2


def go_first(game_dict):
    coin_flip = '''
    ω･)و ̑̑༉⑩
       ̑̑༉₢
     ̑̑⑩
     ̑₢
    ⑩
    
    i know... the animation in ascii is very impressive \n
    '''
    if game_dict['number of rounds'] and game_dict['last game']['is won']:  # there was a winner last game,so he goes
        # first
        res = 'player_x' if game_dict['player_x']['last_game_win'] else 'player_o'
        print(f"{game_dict[res]['name']}, because you won the last round you get to go first")
    elif game_dict['number of rounds'] and not game_dict['last game']['is won']:  # no winner last game,flip a coin
        print("since last game was a draw we're going to flip a coin to see who"
              " goes first\n"
              "ready for it?\n")
        print(coin_flip)
        res = random.choice(['player_x', 'player_o'])
        print(f"{game_dict[res]['name']}, you won the fake...i mean real.. coin flip...mmm\n"
              f"so you get to go first")
    else:  # first round
        print("for the first game we're going to flip a coin to see who"
              " goes first\n"
              "ready for it?\n")
        sleep(4)
        system('cls')
        print(coin_flip)
        res = random.choice(['player_x', 'player_o'])
        sleep(4)
        system('cls')
        print(f"{game_dict[res]['name']}, you won the fake...i mean real.. coin flip...mmm\n"
              f"so you get to go first")
        sleep(4)
        system('cls')
    return res


def result(info, outcome):
    if outcome == 'draw':
        info['player_x']['last_game_win'] = False
        info['player_o']['last_game_win'] = False
        info['last game']['is won'] = False
        info['number of draw'] = info['number of draw'] + 1
        print('it looks like we have a draw')
    else:
        loser = 'player_x' if outcome == 'player_o' else 'player_o'
        info[outcome]['wins'] = info[outcome]['wins'] + 1
        info[outcome]['last_game_win'] = True
        info[loser]['last_game_win'] = False
        info['last game']['is won'] = True
        print(f"{info[outcome]['name']} is this round winner\n"
              f"{info[loser]['name']} that's mean your the loser by the way....")
    info['number of rounds'] = info['number of rounds'] + 1
    sleep(5)
    system('cls')
    print(f"and now for the aggregate result:\n"
          f"you played {info['number of rounds']} games\n"
          f"{info['player_x']['name']} won {info['player_x']['wins']} game's\n"
          f"{info['player_o']['name']} won {info['player_o']['wins']} game's\n"
          f"and there were {info['number of draw']} draw's")
    return info
