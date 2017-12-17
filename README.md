# Josh and Oliver CS127 Final Project

## Chess
Our plan is to make a working game of chess in python. We plan to use the existing python chess package but our project will involve building a wrapper to allow the system to prompt the user for moves and make the game function like an actual chess game with messages for things like captures, check, and illegal moves instead of the slightly perverse commands needed to use the package directly. Additionally, we added extra features to make the game more aesthetically pleasing, such as a bold feature when the king is in check, an undo command, and easier indicators of the pieces. 

Link to package: https://pypi.python.org/pypi/python-chess

### How to play
- Input moves in standard algebraic notation, for example "e4".
- Include an x to capture a piece, for example "Qxf7" uses the queen to capture the piece at f7.
- Type undo to go back to the previous move.
- Here's a basic game to test it out: e4, e5, Qh5, Nc6, Bc4, Nf6, Qxf7

SAMPLE BOARD w/ COORDINATES:

a8 b8 c8 d8 e8 f8 g8 h8  
a7 b7 c7 d7 e7 f7 g7 h7       Black's Side (notated with lowercase letters)
a6 b6 c6 d6 e6 f6 g6 h6   
a5 b5 c5 d5 e5 f5 g5 h5
a4 b4 c4 d4 e4 f4 g4 h4
a3 b3 c3 d3 e3 f3 g3 h3
a2 b2 c2 d2 e2 f2 g2 h2       White's Side (notated with uppercase letters)
a1 b1 c1 d1 e1 f1 g1 h1

Black's side is on top (notated with lowercase letters) and White's side is on the bottom (notated with uppercase letters)
