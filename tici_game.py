from tic_tac_toe.user_input import user_input
from tic_tac_toe.game_Board import welcome, go_first, result
from os import system

if __name__ == '__main__':
    system('cls')
    game_info = {
        'player_x': {'name': str, 'wins': 0, 'last_game_win': False, 'char': 'X'},
        'player_o': {'name': str, 'wins': 0, 'last_game_win': False, 'char': 'O'},
        'last game': {'is won': False},
        'number of rounds': 0,
        'number of draw': 0,
    }
    name_x, name_o = welcome()
    game_info['player_x']['name'] = name_x
    game_info['player_o']['name'] = name_o
    while True:
        first = go_first(game_info)
        game_outcome = user_input(game_info, first)
        new_info = result(game_info, game_outcome)
        game_info = new_info
        while True:
            again = input('would you like to play another game: yes/no ? :\n')
            if again == 'yes':
                system('cls')
                break
            if again == 'no':
                print('bye bye now')
                exit()
