# W02 Prove: Developer - Tic Tac Toe
# Logan Andrus

def check_win(board):
    if (board[0] == board[1] == board[2] or
    board[3] == board[4] == board[5] or 
    board[6] == board[7] == board[8] or
    board[0] == board[3] == board[6] or
    board[1] == board[4] == board[7] or
    board[2] == board[5] == board[8] or
    board[2] == board[4] == board[6] or
    board[0] == board[4] == board[8]):
        print_board(board)
        return True
    
    else:
        return False

def print_board(board):
    print()
    print(str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]))
    print("---------")
    print(str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]))
    print("---------")
    print(str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]))
    print()

def main():
    board = [1, 2, 3,
            4, 5, 6,
            7, 8, 9]

    choices = list(range(1,10))
    end_game = False
    round = 1
    player = "x"
    while (not end_game) and round != 10 :
        print_board(board)
        while not end_game:
            choice = int(input(player + "'s turn to choose a square(1-9): "))
            if choice in choices:
                choices.remove(choice)
                board[choice - 1] = player
                win = check_win(board)
                if win == True:
                    end_game = True
                    print('Player \'' + player + "\' WINS!")
                    break
                if player == "x":
                    player = "o"
                elif player == "o":
                    player = "x"
                round += 1
                break
            else:
                print("That is not a valid choice")


if __name__ == '__main__':
    main()