import chess

board = chess.Board()

print(chr(27) + "[2J")

def checks():
    if board.is_stalemate():
        return "Stalemate!"
    if board.is_insufficient_material():
        return "Insufficient Material!"
    if board.is_checkmate():
        return "Checkmate!"
    return True

def white_move():
    print(board)
    if checks() is True:
        wmove = input("White's move: ")
        try:
            wmove = board.parse_san(wmove)
            if wmove in board.legal_moves:
                board.push(wmove)
                print(chr(27) + "[2J")
            else:
                print(chr(27) + "[2J")
                print("Illegal move, try again.")
                white_move()
        except:
            print(chr(27) + "[2J")
            print("Try again.")
            white_move()
        else:
            print()
    else:
        print(checks())

def black_move():
    print(board)
    if checks() is True:
        bmove = input("Black's move: ")
        try:
            bmove = board.parse_san(bmove)
            if bmove in board.legal_moves:
                board.push(bmove)
                print(chr(27) + "[2J")
            else:
                print(chr(27) + "[2J")
                print("Illegal move, try again.")
                black_move()
        except:
            print(chr(27) + "[2J")
            print("Try again.")
            black_move()
    else:
        print(checks())

def game():
    if checks() is True:
        white_move()
        black_move()
        game()
    else:
        print(checks)

game()
