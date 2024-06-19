A chess variant class representing a chess variant in which
the traditional pieces are joined by hunter and falcon pieces.
Contains methods to start the game, set the pieces, make
moves, print a visual representation, and more helper methods.
A piece class containing location and symbol data members
as well as methods to determine the legality of moves is
inherited by the chess pieces including king, queen, bishop, etc.
Each of these are further inherited by piece classes with data
members denoting what color team they belong to. Specific pieces -
pawn, hunter, and falcon - have unique move methods depending
on what team they are on. The game ends when either team's king is
captured and removed from the board.
