# coding=utf-8
import random
from sys import exit

def check_for_winning_triad(board_):
    for row in board_:  # rows
        if not row[0] is None and row[0] == row[1] and row[1] == row[2]:
            return row[0]

    for i in range(3):  # columns
        if not board_[0][i] is None and board_[0][i] == board_[1][i] and board_[1][i] == board_[2][i]:
            return board_[0][i]

    if not board_[0][0] is None and board_[0][0] == board_[1][1] and board_[1][1] == board_[2][2]:  # diagonal
        return board_[0][0]

    if not board_[0][2] is None and board_[0][2] == board_[1][1] and board_[1][1] == board_[2][0]:  # other diagonal
        return board_[0][2]

    return False


def board_is_full(board_):
    for row in board_:
        for item in row:
            if item is None:
                return False
    return True


def print_board(board_):
    board_str = ''
    for i in range(3):
        for j in range(3):
            spot = board_[i][j]
            if spot is None:
                board_str += ' '
            else:
                board_str += board_[i][j]

            if j < 2:
                board_str += '|'
            if j == 2:
                board_str += '\n'
                if i < 2:
                    board_str += '-----\n'
    print(board_str)


def get_free_positions(board_):
    free_positions = []
    for i in range(3):
        for j in range(3):
            if board_[i][j] is None:
                free_positions.append(i * 3 + j + 1)  # map i,j coordinates to 1-9 sequence
    return free_positions


def update_board(board_, position, team):
    position -= 1  # make 1-9 range start from 0
    row = position // 3
    column = position % 3
    board_[row][column] = team


if __name__ == '__main__':
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    print('Welcome to tic tac toe game! See numbering of spots below:')
    print('1|2|3\n'
          '-----\n'
          '4|5|6\n'
          '-----\n'
          '7|8|9')

    teams = ('X', 'Y')
    user_team = input("Write X or O and press enter, to select the respetive symbol: [X's play first] ")
    if user_team not in teams:
        print('Bad choice, exiting')
        exit(1)
    print('You have selected team %s' % user_team)

    playing_team = 'X'
    while True:
        free_positions = get_free_positions(board)
        if playing_team == user_team:
            pos_assigned = False
            pos = input('Available positions: %s  Please pick one by entering its number: ' % free_positions)
            while not pos_assigned:
                try:
                    pos = int(pos)
                    pos_assigned = True
                except ValueError:
                    pos = input('Bad choice. Please enter a position to pick, again:')
        else:
            pos = random.choice(free_positions)

        update_board(board, pos, playing_team)

        print('Board status after %s choice:' % ('your' if playing_team == user_team else "computer's"))
        print_board(board)

        res = check_for_winning_triad(board)
        if res:
            if res == user_team:
                print('You win! Congratulations!')
            else:
                print('Computer wins.')
            break

        if board_is_full(board):
            print('Tie! Nobody wins.')
            break

        if playing_team == 'X':
            playing_team = 'Y'
        else:
            playing_team = 'X'
