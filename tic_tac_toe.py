
def main():
    print("Tic-Tac-Toe")
    game_board = create_game_board()
    player_x = []
    player_o = []
    
    # Game Loop, it will stop when the result is Win, Lose or Draw.
    while True:
        
        # PLayer X
        print_board(game_board)
        # Player X input
        player_option = player_input(game_board,"X")
        
        # Validate player input
        player_x.append(game_board[player_option])
        game_board[player_option] = "X"

        # Check win situation
        if check_win(player_x):
            print_board(game_board)
            print("X's Player Win!")
            break

        # Check draw situation
        elif check_draw(player_x):
            print_board(game_board)
            print("Draw!")
            break

        # Player O
        print_board(game_board)
        # Player O input
        player_option = player_input(game_board,"O")

        # Validate player input
        player_o.append(game_board[player_option])
        game_board[player_option] = "O"
        
        
        # Check win situation
        if check_win(player_o):
            print_board(game_board)
            print("O's Player Win!")
            break


def player_input(game_board,player):
    while True:
        try:
            player_option = int(input(f"{player}'s turn to choose a square (1-9): "))

            if player_option > 0 and player_option < 10:
                if game_board[player_option] == "X" or game_board[player_option] == "O":
                    print("Already taken. Choose other")
                else:
                    break
            else:
                print("Error: Wrong Input")

        except ValueError:
            print("Error: Wrong Input")
            
    return player_option
    
def create_game_board():
    game_board = [0,1,2,3,4,5,6,7,8,9]
    return game_board

def print_board(game_board):
    print()
    print(f"{game_board[1]} | {game_board[2]} | {game_board[3]}")
    print("- + - + -")
    print(f"{game_board[4]} | {game_board[5]} | {game_board[6]}")
    print("- + - + -")
    print(f"{game_board[7]} | {game_board[8]} | {game_board[9]}")
    print()

def check_win(player_status):
    win_situation = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    sum = 0

    for x in win_situation:
        for y in player_status:
            if y in x:
                sum += 1
        if sum == 3:
            sum = 0
            return True
        else:
            sum = 0
    return False

def check_draw(player_x):
    if len(player_x) == 5:
        return True
    else:
        return False

if __name__ == "__main__":
    main()