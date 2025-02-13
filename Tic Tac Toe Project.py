#Program to build Tic Tac Toe game in Python
#print/display board

board=[]
x=0
while x!=3:
    board.append([" " for i in range(3)])   #0,1,2
    x += 1

#function to print board
def print_board():
    for i in board[0:3]:
        print("| {} | {} | {} |".format(i[0],i[1],i[2]))
print_board()

def player_move(icon):
    if icon=='X':
        number = 1
    elif icon == 'O':
        number = 2

    while True:
        print("Your turn player {}".format(icon))
        choice = input('enter your move (1-9):')
        if choice in '123456789' and choice != ' ':
            choice=int(choice)
            if choice in [1,2,3]:
                if board[0][choice-1] == ' ':
                    board[0][choice-1] =icon
                    print_board()
                    break
                else:
                    print('The space is already taken')

            elif choice in [4,5,6]:
                if board[1][choice-4] == ' ':
                    board[1][choice-4]=icon
                    print_board()
                    break
                else:
                    print('The space is already taken')

            elif choice in [7,8,9]:
                if board[2][choice-7]==' ':
                    board[2][choice-7]=icon
                    print_board()
                    break
                else:
                    print('The space is already taken')

            else:
                print('The space does not exists')
                continue
        else:
            print('Invalid input')

def victory(icon):
        if((board[0][0]==icon and board[0][1]==icon and board[0][2]==icon) or \
            (board[1][0]==icon and board[1][1]==icon and board[1][2]==icon)  or \
            (board[2][0]==icon and board[2][1]==icon and board[2][2]==icon) or \
            (board[0][0]==icon and board[1][0]==icon and board[2][0]==icon) or \
            (board[0][1] == icon and board[1][1] == icon and board[2][1] == icon) or \
            (board[0][2] == icon and board[1][2] == icon and board[2][2] == icon)or\
            (board[0][0]==icon and board[1][1]==icon and board[2][2]==icon) or \
            (board[2][0]==icon and board[1][1]==icon and  board[0][2]==icon)):
            return True
        else:
            return False

def draw():
    if ' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2]:
        return True
    else:
        return False

while True:
    player_move('X')
    if victory('X'):
        print('X wins..congrats')
        break
    elif draw():
        print('its a draw')
        break
    player_move('O')
    if victory('O'):
        print('O wins..congrats')
        break
    elif draw():
        print('its a draw')
        break

print('Thanks for playing')










