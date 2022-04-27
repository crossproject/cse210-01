
def main():
    print("Tic-Tac-Toe")
    print()
    game_board = create_game_board()
    player_x = []
    player_o = []
    while True:
        
        print_board(game_board)
        player_option = int(input("x's turn to choose a square (1-9): "))
        while True:
            if game_board[player_option] == "X" or game_board[player_option] == "O":
                print("Already taken. Choose other")
                player_option = int(input("x's turn to choose a square (1-9): "))
            else:
                player_x.append(game_board[player_option])
                game_board[player_option] = "X"
                break
        if check_win(player_x):
            print_board(game_board)
            print("X's Player Win!")
            break

        print_board(game_board)
        player_option = int(input("o's turn to choose a square (1-9): "))
        while True:
            if game_board[player_option] == "X" or game_board[player_option] == "O":
                print("Already taken. Choose other")
                player_option = int(input("o's turn to choose a square (1-9): "))
            else:
                player_o.append(game_board[player_option])
                game_board[player_option] = "O"
                break

        if check_win(player_o):
            print_board(game_board)
            print("O's Player Win!")
            break
    


def create_game_board():
    game_board = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
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

if __name__ == "__main__":
    main()