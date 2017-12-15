# Josh and Oliver Project

## Chess
Our plan is to make a working game of chess in python. We plan to use the existing python chess package but our project will involve building a wrapper to allow the system to prompt the user for moves and make the game function like an actual chess game with messages for things like captures, check, and illegal moves instead of the slightly perverse commands needed to use the package directly.

Link to package: https://pypi.python.org/pypi/python-chess

### How to play
- Input moves in standard algebraic notation, for example "e4".
- Include an x to capture a piece, for example "Qxf7" uses the queen to capture the piece at f7.
- Here's a basic game to test it out:
-- e4, e5, Qh5, Nc6, Bc4, Nf6, Qxf7

If we finish this part ahead of schedule, we'll try to do some of the extensions including:
- most common words with removed
- stemming library/algorithm
- web app (maybe)
- add info to inverted index
- n grams
