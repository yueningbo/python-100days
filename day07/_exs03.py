import os

def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('---+---+---')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('---+---+---')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def main():
    init_borad = {
        'TL': '   ', 'TM': '   ', 'TR': '   ',
        'ML': '   ', 'MM': '   ', 'MR': '   ',
        'BL': '   ', 'BM': '   ', 'BR': '   '}
    begin = True
    while begin:
        curr_borad = init_borad.copy()
        begin = False
        turn = ' x '
        counter = 0
        os.system('cls')
        print_board(curr_borad)
        while counter < 9:
            move = input('轮到%s走棋， 请输入位置: ' % turn)
            if curr_borad[move] == '   ':
                counter += 1
                curr_borad[move] = turn
                if turn == ' x ':
                    turn = ' o '
                else:
                    turn = ' x '
            os.system('cls')
            print_board(curr_borad)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'


if __name__ == '__main__':
    main()
