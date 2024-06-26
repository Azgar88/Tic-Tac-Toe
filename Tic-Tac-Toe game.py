def display_board(board):
    print(' '+board[7]+'|'+board[8]+'|'+board[9])
    print(' '+board[4]+'|'+board[5]+'|'+board[6])
    print(' '+board[1]+'|'+board[2]+'|'+board[3])
test_board=['#','X','O','X','O','X','O','X','O','X']

def player_input():
    marker=''
    while not (marker=='X' or marker=='O'):
        marker = input('Player1, Do you want to be X or O? : ').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')    

import random
def choose_first():
    if random.randint(0,1)==0:
        return 'Player1'
    else:
        return 'Player2'

def space_check(board,position):
    return board[position]==' '

def player_choice(board):
    while True:
        position=input('Choose your option (1-9)')
        if(position.isdigit() and int(position) in [1,2,3,4,5,6,7,8,9]):
            return int(position)
        else:
            print("re-enter the input")

def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[1] == mark and board[2] == mark and board[3] == mark) or(board[7] == mark and board[4] == mark and board[1] == mark) or (board[8] == mark and board[5] == mark and board[2] == mark) or(board[9] == mark and board[6] == mark and board[3] == mark) or(board[7] == mark and board[5] == mark and board[3] == mark) or(board[9] == mark and board[5] == mark and board[1] == mark))

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def replay():
    return input('Do you want to play again? Enter Yes or No').lower().startswith('y')

print('Welcome to Tic Tac Toe!')
while True:
    theBoard=[' ']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+' '+'will go first')
    play_game=input('Are you ready to play? Enter Y or N.').upper()
    if play_game=='Y':
        game_on=True
    else:
        game_on=False   
    while game_on:
        if turn == 'Player1':
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)
            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('Player1 has won the game')
                game_on=False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is Draw!')
                    break
                else:
                    turn='Player2'
        else:
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)
            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print('Player2 has won the game')
                game_on=False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is Draw!')
                    break
                else:
                    turn='Player1'
    if not replay():
        break
