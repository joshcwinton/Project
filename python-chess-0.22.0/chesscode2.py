import chess


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


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
        except ValueError:
            print(chr(27) + "[2J")
            print("Invalid input, try again.")
            white_move()
        else:
            print()
    else:
        print(checks())


def black_move():
    print(board)
    if checks() is True:
        '''if board.is_check:
            for i in board.fe:
                if i is 'k':
                    i = color.ITALIC + 'k' + color.END'''
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
        except ValueError:
            print(chr(27) + "[2J")
            print("Invalid input, try again.")
            black_move()
    else:
        print(color.BOLD + checks() + color.END)


def game():
    if checks() is True:
        white_move()
        black_move()
        game()


game()
