# set a blank board
board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

# checks game finished/valid
def checker(b):
    x_wins = False
    o_wins = False
    tot_x = 0
    tot_o = 0
    tot_space = 0

    # check totals, down and across
    for i in range(0, 3):
        x = 0
        o = 0
        x_down = 0
        o_down = 0
        for j in range(0, 3):
            if b[i][j] == 'X':
                x += 1
                tot_x += 1
            if b[i][j] == 'O':
                o += 1
                tot_o += 1
            if b[i][j] == '_':
                tot_space += 1
            if b[j][i] == 'X':
                x_down += 1
            if b[j][i] == 'O':
                o_down += 1
        if x == 3 or x_down == 3:
            x_wins = True
        if o == 3 or o_down == 3:
            o_wins = True
    # checks verticles
    if (b[0][0] == b[1][1] == b[2][2]) or (b[2][0] == b[1][1] == b[0][2]):
        if b[1][1] == 'X':
            x_wins = True
        if b[1][1] == 'O':
            o_wins = True
    # return game state
    if x_wins & o_wins or tot_x - tot_o > 1 or tot_x - tot_o < -1:
        return "Impossible"
    if x_wins:
        return "X wins"
    if o_wins:
        return "O wins"
    if tot_space > 0:
        return "Game not finished"
    if tot_x + tot_o == 9:
        return "Draw"

#print a board
def print_board(b):
    top = "---------"
    side = "|"
    print(top)
    for i in range(0, 3):
        print(f"{side} {b[i][0]} {b[i][1]} {b[i][2]} {side}")
    print(top)

# get move from user
def get_move(b, turn):
    column = [2, 1, 0]
    
    coor = input("Enter the coordinates:").split()
    # check input is valid
    try:
        x = int(coor[0])
        y = int(coor[1])
        if x > 3 or x < 1 or y > 3 or y < 1:
            print("Coordinates should be from 1 to 3!")
            return get_move(board)
    except:
        print("Enter a number")
        return get_move(b, turn)
    y = column[y-1]

    if board[y][x - 1] == "_" :
        board[y][x - 1] = turn
    else:
        print("That space is occupied")
        get_move(board, turn)

# start a game 
def start_game():
    # checks if game is complete
    finished = checker(board)
    #set turn
    turn = "X"
    print_board(board)
    
    while finished == "Game not finished":
        get_move(board, turn)
        print_board(board)
        finished = checker(board)
        # change turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = "X"
    print(finished)


start_game()
