import chess


def game():
    # main function
    board = chess.Board()
    move(board)
    return None



def move(boardname):
    print(boardname)
    print()
    for i in range(300):
        if checks(boardname) is True:
            if i%2 == 0:
                wmove = input("What's your move, white? ")
                '''if chess.Move.from_uci(wmove) in boardname.legal_moves:
                    boardname.push_san(wmove)
                else:
                    break'''
                boardname.push_san(wmove)
                print()
                print(boardname)
                print()
            else:
                bmove = input("What's your move, black? ")
                '''if chess.Move.from_uci(bmove) in boardname.legal_moves:
                    boardname.push_san(bmove)
                else:
                    break'''
                boardname.push_san(bmove)
                print()
                print(boardname)
                print()
        else:
            print(gameover(boardname))
            break
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
    if boardname.is_stalemate():
        return "Stalemate!"
    if boardname.is_insufficient_material():
        return "Insufficient Material!"
    if boardname.is_game_over():
        return "Game Over!"
    return True


game()
