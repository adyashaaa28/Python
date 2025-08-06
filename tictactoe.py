def check_win(board, player):
    # Check rows, columns and diagonals for a win
    for i in range(3):
        if all([x == player for x in board[i]]): 
            return True
        if all([board[j][i] == player for j in range(3)]): 
            return True
    if all([board[i][i] == player for i in range(3)]): 
        return True
    if all([board[i][2-i] == player for i in range(3)]): 
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turns = 0
    while turns < 9:
        p = players[turns % 2]
        print(f"Player {p}'s turn.")
        try:
            row = int(input("Row (0/1/2): "))
            col = int(input("Col (0/1/2): "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == " ":
                    board[row][col] = p
                    turns += 1
                    if check_win(board, p):
                        print(f"Player {p} wins!")
                        return
                else:
                    print("Cell already taken, try again.")
            else:
                print("Invalid row or column number, try again.")
        except ValueError:
            print("Please enter valid integers for row and column.")
    print("It's a draw!")

# Run the game
tic_tac_toe()
