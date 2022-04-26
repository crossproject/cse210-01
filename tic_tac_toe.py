def main():
    pass



def check_win(player_status):
    win_situation = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    if player_status in win_situation:
        return True
    else:
        return False

if __name__ == "__main__":
    main()