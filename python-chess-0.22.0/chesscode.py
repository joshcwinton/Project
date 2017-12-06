import chess

def game():
    # main function
    board = chess.Board()
    move(board)
    return None

def move(boardname):
    for i in range(300):
        if checks(boardname) is True:
            if i%2 == 0:
                wmove = input("What's your move, white? ")
                boardname.push_san(wmove)
                print()
                print(boardname)
                print()
                print()
            else:
                bmove = input("What's your move, black? ")
                boardname.push_san(bmove)
                print()
                print(boardname)
                print()
                print()
        else:
            print(gameover(boardname))
    # function looped in game
    return None

def checks(boardname):
    if boardname.is_stalemate():
        return False
    if boardname.is_insufficient_material():
        return False
    if boardname.is_game_over():
        return False
    if boardname.is_check():
        print("Check!")
        return True
    return True

def gameover(boardname):
    if name.is_stalemate():
        return "Stalemate!"
    if name.is_insufficient_material():
        return "Insufficient Material!"
    if name.is_game_over():
        return "Game Over!"
    return True

game()
