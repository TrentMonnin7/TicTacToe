#create a two player tic tac toe game
import random
test_board = [' ']*10

def display_board(board):
    print('\n'*100)
    print(board[7]+'  |  '+board[8]+'  |  '+board[9])
    print('---'+'|'+'-----'+'|'+'---')
    print(board[4]+'  |  '+board[5]+'  |  '+board[6])
    print('---'+'|'+'-----'+'|'+'---')
    print(board[1]+'  |  '+board[2]+'  |  '+board[3])  

display_board(test_board)