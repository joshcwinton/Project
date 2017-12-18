
# gets chess package
import chess


# allows use of "class.BOLD" instead of typing this string every time
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


# creates an instance of a chess board from package
board = chess.Board()

# clears terminal window
print(chr(27) + "[2J")


# checks that either result in game over or return true
def checks():
    if board.is_stalemate():
        return "Stalemate!"
    if board.is_insufficient_material():
        return "Insufficient Material! The game is a draw."
    if board.is_checkmate():
        return "Checkmate!"
    return True


# checks if king is in check using package, used to print check
def k_attk():
    if board.is_check():
        return True
    return False


# runs for white's turn
def white_move():
    print(board)
    # prints check if king is in check
    if k_attk() is True:
        print(color.BOLD + "Check!" + color.END)
    if checks() is True:
        wmove = input("White's move: ")
        # tries to make a move with the input given, if it's illegal, we print
        # a message and call the function again
        try:
            wmove = board.parse_san(wmove)
            if wmove in board.legal_moves:
                board.push(wmove)
                print(chr(27) + "[2J")
        except ValueError:
            # code for "undo": calls board.pop() which jumps back to the last
            # move in the stack
            if wmove == "undo":
                board.pop()
                print(chr(27) + "[2J")
                print("Modifying Black's last move.")
                black_move()
            else:
                print(chr(27) + "[2J")
                print("Invalid input, try again.")
                white_move()
    else:
        # prints what's wring if the game can't proceed
        print(checks())


# same as white function just the opposite color
def black_move():
    print(board)
    if k_attk() is True:
        print(color.BOLD + "Check!" + color.END)
    if checks() is True:
        bmove = input("Black's move: ")
        try:
            bmove = board.parse_san(bmove)
            if bmove in board.legal_moves:
                board.push(bmove)
                print(chr(27) + "[2J")
        except ValueError:
            if bmove == "undo":
                board.pop()
                print(chr(27) + "[2J")
                print("Modifying White's last move.")
                white_move()
            else:
                print(chr(27) + "[2J")
                print("Invalid input, try again.")
                black_move()
    else:
        print(color.BOLD + checks() + color.END)


# main game function, calls both turns if all checks are true then recursively
# calls itself
def game():
    # included call to checks here even though it's in both white_move and
    # black_move so that game doesn't become an endless loop if we reach
    # checkmate
    if checks() is True:
        white_move()
        black_move()
        game()


game()
