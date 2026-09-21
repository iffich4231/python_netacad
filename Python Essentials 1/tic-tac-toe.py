from random import randrange

board = [
    ['1', '2', '3'],
    ['4', 'X', '6'],
    ['7', '8', '9']
]

def display_board(board):
    print("+-------" * 3 + "+")
    for row in board:
        print("|       " * 3 + "|")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")

def free_blocks(board):
    counter = 0
    for row in board:
        for item in row:
            if item not in ['X', 'O']:
                counter += 1
    return counter

def victory_for(board, sign):
    for row in board:
        if row[0] == row[1] == row[2] == sign:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True

    return False

display_board(board)
while True:
    while True:
        try:
            move = int(input("Enter your move: "))
        except ValueError:
            print("Enter a valid value: ")
            continue                            # asks for input again immediately

        if 1 <= move <= 9:
            row = (move - 1) // 3
            col = (move - 1) % 3

            if board[row][col] not in ['X', 'O']:
                board[row][col] = 'O'
                break
            else:
                print("That block is already taken!")
        else:
            print("Enter a number between 1 and 9")

    display_board(board)

    if victory_for(board, 'O'):
        print("You won!")
        break

    if free_blocks(board) == 0:
        print("Its a tie!")
        break

    while True:
        comp_move = randrange(1, 10, 1)
        row = (comp_move - 1) // 3
        col = (comp_move - 1) % 3
        if board[row][col] not in ['X', 'O']:
            board[row][col] = 'X'
            break

    display_board(board)
    
    if victory_for(board, 'X'):
        print("Computer won!")
        break
    
    if free_blocks(board) == 0:
        print("Its a tie!")
        break