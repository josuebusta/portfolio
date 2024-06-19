# Author: Josue Bustamante
# GitHub username: josuebusta
# Date: 3/17/2024
# Description: A chess variant class representing a chess variant in which
#              the traditional pieces are joined by hunter and falcon pieces.
#              Contains methods to start the game, set the pieces, make
#              moves, print a visual representation, and more helper methods.
#              A piece class containing location and symbol data members
#              as well as methods to determine the legality of moves is
#              inherited by the chess pieces including king, queen, bishop, etc.
#              Each of these are further inherited by piece classes with data
#              members denoting what color team they belong to. Specific pieces -
#              pawn, hunter, and falcon - have unique move methods depending
#              on what team they are on. The game ends when either team's king is
#              captured and removed from the board.
class ChessVar:
    """
    Represents a game of a chess variant. Initializes the game status
    to unfinished, the turn count to 0, the board and off-board to empty
    dictionaries, and the captures pieces to an empty list.
    It also calls the start game method.
    """

    def __init__(self):
        self._game_state = 'UNFINISHED'
        self._turn_count = 0
        self._board = {}
        self._off_board = {}
        self._captured = []
        self.start_game()

    def start_game(self):
        """
        Initializes the game board if the turn count is 0, returning
        False otherwise. It also calls the set_pieces method to
        place all game pieces at their initial positions and increments
        the turn count to the first turn.
        """
        # CHECKS if game has not started yet
        if self._turn_count == 0:
            x_axis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
            y_axis = ['1', '2', '3', '4', '5', '6', '7', '8']

            # INITIALIZES board and off-board dictionaries
            self._board = {x_axis[val]: None for val in range(len(x_axis))}
            for index in self._board:
                self._board[index] = {y_axis[val]: None for val in range(len(y_axis))}

            self._off_board = {'WHITE': {'1': None, '2': None}, 'BLACK': {'1': None, '2': None}}

        else:
            return False

        self.set_pieces()
        self._turn_count += 1

    def set_pieces(self):
        """
        Places all game piece objects at their initial positions on and off
        the board at the start of a game, initializing the objects at their locations,
        returning false if the turn count is not 0.
        """
        if self._turn_count == 0:
            self._board['a']['1'] = WhiteRook('a1')
            self._board['b']['1'] = WhiteKnight('b1')
            self._board['c']['1'] = WhiteBishop('c1')
            self._board['d']['1'] = WhiteQueen('d1')
            self._board['e']['1'] = WhiteKing('e1')
            self._board['f']['1'] = WhiteBishop('f1')
            self._board['g']['1'] = WhiteKnight('g1')
            self._board['h']['1'] = WhiteRook('h1')
            for index in self._board:
                self._board[index]['2'] = WhitePawn(f'{index}2')

            self._off_board['WHITE']['1'] = WhiteHunter('OB')
            self._off_board['WHITE']['2'] = WhiteFalcon('OB')

            self._board['a']['8'] = BlackRook('a8')
            self._board['b']['8'] = BlackKnight('b8')
            self._board['c']['8'] = BlackBishop('c8')
            self._board['d']['8'] = BlackQueen('d8')
            self._board['e']['8'] = BlackKing('e8')
            self._board['f']['8'] = BlackBishop('f8')
            self._board['g']['8'] = BlackKnight('g8')
            self._board['h']['8'] = BlackRook('h8')
            for index in self._board:
                self._board[index]['7'] = BlackPawn(f'{index}7')

            self._off_board['BLACK']['1'] = BlackHunter('OB')
            self._off_board['BLACK']['2'] = BlackFalcon('OB')
        else:
            return False

    def show_board(self, pos=9):
        """
        Recursive function displaying a visual representation
        of the chess board using the contents of the board dictionary.
        """

        # PRINTS black team off-board pieces
        if pos == 9:
            board_row = [['OFF BOARD']]
            for val in self._off_board['BLACK']:
                if self._off_board['BLACK'][val] is None:
                    board_row.append([' '])
                else:
                    board_row.append([self._off_board['BLACK'][val].get_symbol()])
            print(board_row)
            self.show_board(pos - 1)

            # PRINTS white team off-board pieces
            board_row = [['OFF BOARD']]
            for val in self._off_board['WHITE']:
                if self._off_board['WHITE'][val] is None:
                    board_row.append([' '])
                else:
                    board_row.append([self._off_board['WHITE'][val].get_symbol()])
            print(board_row)
            return

        # CHECKS if end of board is reached
        if pos == 0:
            board_row = [[' ']]
            for val in self._board:
                board_row.append([val])
            print(board_row)
            return

        num = f"{pos}"
        board_row = [[f'{pos}']]

        # PRINTS board square contents
        for val in self._board:
            if self._board[val][num] is None:
                board_row.append([' '])
            else:
                board_row.append([self._board[val][num].get_symbol()])
        print(board_row)
        self.show_board(pos - 1)

    def make_move(self, from_square, to_square):
        """
        Takes as parameters two strings representing the square
        a piece is moving from and the square it is moving to.
        Calls the corresponding move method of whichever Piece
        objects occupies the source square to determine the
        legality of the move.
        Returns False if the move is illegal or the game
        has ended.
        If the move is legal, the move is made, any captured
        piece is removed from the board, the player turn is updated
        as well as the game state if necessary, and the method
        returns True.
        """
        x_axis_1 = from_square[0]
        y_axis_1 = from_square[1]
        x_axis_2 = to_square[0]
        y_axis_2 = to_square[1]

        # CHECKS if game has finished
        if self._game_state != 'UNFINISHED':
            return False

        # CHECKS if input is not in range
        if x_axis_1 not in self._board or x_axis_2 not in self._board:
            if y_axis_1 not in self._board[0] or y_axis_2 not in self._board[0]:
                return False

        # CHECKS if input square is empty
        if self._board[x_axis_1][y_axis_1] is None:
            return False
        else:
            game_piece = self._board[x_axis_1][y_axis_1]

        # CHECKS if piece is being moved during the right turn
        if game_piece.get_color() == "BLACK" and self._turn_count % 2 != 0:
            return False
        elif game_piece.get_color() == "WHITE" and self._turn_count % 2 == 0:
            return False
        else:
            result = (game_piece.move(from_square, to_square, self._board))

        # IF move is legal
        if result is True:
            # IF destination is occupied by opponent
            if self._board[x_axis_2][y_axis_2] is not None:
                captured = self._board[x_axis_2][y_axis_2]
                self.captured_list(captured.get_symbol(), self._turn_count)
            # IF destination is empty
            self._board[x_axis_2][y_axis_2] = game_piece
            self._board[x_axis_1][y_axis_1] = None
            game_piece.set_location(to_square)
            self._turn_count += 1
            return True
        else:
            return False

    def enter_fairy_piece(self, piece, square):
        """
        Takes as parameters two strings, one representing the
        fairy piece object and the other representing the square it
        will enter. If the move is legal, the piece starts in
        that position, the turn count is updated, and the method
        returns True.
        """
        x_axis_1 = square[0]
        y_axis_1 = square[1]
        x_axis_2 = None
        y_axis_2 = None
        white_pieces = ["♕", "♖", "♗", "♘"]
        black_pieces = ["♛", "♜", "♝", "♞"]
        white_captured_count = 0
        black_captured_count = 0
        game_piece = None
        color = None

        # CHECKS if destination square is empty
        if self._board[x_axis_1][y_axis_1] is not None:
            return False

        # FINDS piece in off-board
        for index in self._off_board:
            for val in self._off_board[index]:
                if (self._off_board[index][val] is not None and
                        self._off_board[index][val].get_symbol() == piece):
                    game_piece = self._off_board[index][val]
                    x_axis_2 = index
                    y_axis_2 = val
                    color = game_piece.get_color()
        
        # CHECKS if game piece is found in off-board
        if game_piece is None:
            return False
        
        # CHECKS if piece is being moved during the right turn
        if color == "BLACK" and self._turn_count % 2 != 0:
            return False
        elif color == "WHITE" and self._turn_count % 2 == 0:
            return False
        
        # CHECKS if list of captured pieces is empty
        if len(self._captured) == 0:
            return False
        
        # COUNTS the number of white pieces captured
        for index in self._captured:
            if index[0] in white_pieces:
                white_captured_count += 1

        # COUNTS the number of black pieces captured
        for index in self._captured:
            if index[0] in black_pieces:
                black_captured_count += 1

        # IF piece being called is on the white team
        if color == "WHITE":
            # CHECKS if destination is out of bounds
            if y_axis_1 > "2":
                return False
            
            # IF only one white piece has been captured
            if white_captured_count == 1:
                for index in self._off_board['WHITE']:
                    if self._off_board['WHITE'][index] is None:     # IF a fairy piece has been played
                        return False
                self._board[x_axis_1][y_axis_1] = game_piece        # IF not, plays fairy piece
                self._off_board[x_axis_2][y_axis_2] = None
                game_piece.set_location(square)
                self._turn_count += 1
            
            # IF two or more white pieces have been captured
            if white_captured_count >= 2:
                self._board[x_axis_1][y_axis_1] = game_piece        # PLAYS fairy piece
                self._off_board[x_axis_2][y_axis_2] = None
                game_piece.set_location(square)
                self._turn_count += 1
        
        # IF piece being called is on the white team
        elif color == "BLACK":
            if y_axis_1 < "7":
                return False

            # IF only one white piece has been captured
            if black_captured_count == 1:
                for index in self._off_board['BLACK']:
                    if self._off_board['BLACK'][index] is None:     # IF a fairy piece has been played
                        return False
                self._board[x_axis_1][y_axis_1] = game_piece        # IF not, plays fairy piece
                self._off_board[x_axis_2][y_axis_2] = None
                game_piece.set_location(square)
                self._turn_count += 1

            if black_captured_count >= 2:
                self._board[x_axis_1][y_axis_1] = game_piece        # PLAYS fairy piece
                self._off_board[x_axis_2][y_axis_2] = None
                game_piece.set_location(square)
                self._turn_count += 1

    def captured_list(self, piece_symbol, turn):
        """
        Stores the data for the last piece object captured in the game
        and the turn it was captured on.
        """
        
        # ADDS piece captured to list
        self._captured.append((piece_symbol, turn))
        for index in self._captured:
            # IF the piece captured is the black king
            if "♚" in index:
                self._game_state = "WHITE_WON"
            # IF the piece captures is the white king
            if "♔" in index:
                self._game_state = "BLACK_WON"
        return

    def get_game_state(self):
        """
        Returns the game's state.
        """
        return self._game_state
    
    def get_captured_list(self):
        """
        Returns the list of captured pieces.
        """
        return self._captured

    def get_turn_count(self):
        """
        Returns the current turn count
        """
        return self._turn_count


class Piece:
    """
    Represents a game piece with a symbol, location, and color.
    Contains recursive methods for calculating the move set in
    each cardinal direction.
    """

    def __init__(self, location):
        self._symbol = None
        self._location = location
        self._color = None

    def get_symbol(self):
        """
        Returns the piece's symbol.
        """
        return self._symbol

    def get_location(self):
        """
        Returns the piece's location.
        """
        return self._location

    def set_location(self, square):
        """
        Takes a string representing a square as a parameter
        and sets the piece object's location data member to the
        corresponding square.
        """
        self._location = square
        return

    def get_color(self):
        """
        Returns the piece's color.
        """
        return self._color

    def rec_move_north(self, x_axis_1, y_axis_1, game_board, move_set):
        """
        Recursive method which takes the current x and y axes, the game board,
        and the move set list as parameters and returns an updated move set list
        containing the legal moves northward.
        """
        # CHECKS if square is out-of-bounds
        if y_axis_1 > 8:
            return move_set

        # IF current square is occupied by piece on opposite team
        if (game_board[x_axis_1][f"{y_axis_1}"] is not None and
                game_board[x_axis_1][f"{y_axis_1}"].get_color() != self._color):
            move_north = f"{x_axis_1}{y_axis_1}"
            move_set.append(move_north)
            return move_set

        # IF current square is occupied by piece on same team
        if (game_board[x_axis_1][f"{y_axis_1}"] is not None and
                game_board[x_axis_1][f"{y_axis_1}"].get_color() == self._color):
            return move_set

        # IF current square is empty
        if game_board[x_axis_1][f"{y_axis_1}"] is None:
            move_north = f"{x_axis_1}{y_axis_1}"
            move_set.append(move_north)
            self.rec_move_north(x_axis_1, int(y_axis_1) + 1, game_board, move_set)

    def rec_move_south(self, x_axis_1, y_axis_1, game_board, move_set):
        """
        Recursive method which takes the current x and y axes, the game board,
        and the move set list as parameters and returns an updated move set list
        containing the legal moves southward.
        """
        # CHECKS if square is out-of-bounds
        if y_axis_1 < 1:
            return move_set

        # IF current square is occupied by piece on opposite team
        if (game_board[x_axis_1][f"{y_axis_1}"] is not None and
                game_board[x_axis_1][f"{y_axis_1}"].get_color() != self._color):
            move_south = f"{x_axis_1}{y_axis_1}"
            move_set.append(move_south)
            return move_set

        # IF current square is occupied by piece on same team
        if (game_board[x_axis_1][f"{y_axis_1}"] is not None and
                game_board[x_axis_1][f"{y_axis_1}"].get_color() == self._color):
            return move_set

        # IF current square is empty
        if game_board[x_axis_1][f"{y_axis_1}"] is None:
            move_south = f"{x_axis_1}{y_axis_1}"
            move_set.append(move_south)
            self.rec_move_south(x_axis_1, int(y_axis_1) - 1, game_board, move_set)

    def rec_move_west(self, x_axis_1, y_axis_1, game_board, move_set):
        """
        Recursive method which takes the current x and y axes, the game board,
        and the move set list as parameters and returns an updated move set list
        containing the legal moves westward.
        """
        # CHECKS if square is out-of-bounds
        if x_axis_1 < "a":
            return move_set

        # IF current square is occupied by piece on opposite team
        if (game_board[x_axis_1][f"{y_axis_1}"] is not None and
                game_board[x_axis_1][y_axis_1].get_color() != self._color):
            move_west = f"{x_axis_1}{y_axis_1}"
            move_set.append(move_west)
            return move_set

        # IF current square is occupied by piece on same team
        if (game_board[x_axis_1][f"{y_axis_1}"] is not None and
                game_board[x_axis_1][y_axis_1].get_color() == self._color):
            return move_set

        # IF current square is empty
        if game_board[x_axis_1][f"{y_axis_1}"] is None:
            move_west = f"{x_axis_1}{y_axis_1}"
            move_set.append(move_west)
            self.rec_move_west(chr(ord(x_axis_1) - 1), y_axis_1, game_board, move_set)

    def rec_move_east(self, x_axis_1, y_axis_1, game_board, move_set):
        """
        Recursive method which takes the current x and y axes, the game board,
        and the move set list as parameters and returns an updated move set list
        containing the legal moves eastward.
        """
        # CHECKS if square is out-of-bounds
        if x_axis_1 > "h":
            return move_set

        # IF current square is occupied by piece on opposite team
        if (game_board[x_axis_1][f"{y_axis_1}"] is not None and
                game_board[x_axis_1][y_axis_1].get_color() != self._color):
            move_east = f"{x_axis_1}{y_axis_1}"
            move_set.append(move_east)
            return move_set

        # IF current square is occupied by piece on same team
        if (game_board[x_axis_1][f"{y_axis_1}"] is not None and
                game_board[x_axis_1][y_axis_1].get_color() == self._color):
            return move_set

        # IF current square is empty
        if game_board[x_axis_1][f"{y_axis_1}"] is None:
            move_east = f"{x_axis_1}{y_axis_1}"
            move_set.append(move_east)
            self.rec_move_east(chr(ord(x_axis_1) + 1), y_axis_1, game_board, move_set)

    def rec_move_northwest(self, x_axis_1, y_axis_1, game_board, move_set):
        """
        Recursive method which takes the current x and y axes, the game board,
        and the move set list as parameters and returns an updated move set list
        containing the legal moves northwest-ward.
        """
        # CHECKS if square is out-of-bounds
        if x_axis_1 < "a" or y_axis_1 > 8:
            return move_set

        # IF current square is occupied by piece on opposite team
        if (game_board[x_axis_1][f"{y_axis_1}"] is not None and
                game_board[x_axis_1][f"{y_axis_1}"].get_color() != self._color):
            move_northwest = f"{x_axis_1}{y_axis_1}"
            move_set.append(move_northwest)
            return move_set

        # IF current square is occupied by piece on same team
        if (game_board[x_axis_1][f"{y_axis_1}"] is not None and
                game_board[x_axis_1][f"{y_axis_1}"].get_color() == self._color):
            return move_set

        # IF current square is empty
        if game_board[x_axis_1][f"{y_axis_1}"] is None:
            move_northwest = f"{x_axis_1}{y_axis_1}"
            move_set.append(move_northwest)
            self.rec_move_northwest(chr(ord(x_axis_1) - 1), int(y_axis_1) + 1, game_board, move_set)

    def rec_move_northeast(self, x_axis_1, y_axis_1, game_board, move_set):
        """
        Recursive method which takes the current x and y axes, the game board,
        and the move set list as parameters and returns an updated move set list
        containing the legal moves northeast-ward.
        """
        # CHECKS if square is out-of-bounds
        if x_axis_1 > "h" or y_axis_1 > 8:
            return move_set

        # IF current square is occupied by piece on opposite team
        if (game_board[x_axis_1][f"{y_axis_1}"] is not None and
                game_board[x_axis_1][f"{y_axis_1}"].get_color() != self._color):
            move_northeast = f"{x_axis_1}{y_axis_1}"
            move_set.append(move_northeast)
            return move_set

        # IF current square is occupied by piece on same team
        if (game_board[x_axis_1][f"{y_axis_1}"] is not None and
                game_board[x_axis_1][f"{y_axis_1}"].get_color() == self._color):
            return move_set

        # IF current square is empty
        if game_board[x_axis_1][f"{y_axis_1}"] is None:
            move_northeast = f"{x_axis_1}{y_axis_1}"
            move_set.append(move_northeast)
            self.rec_move_northeast(chr(ord(x_axis_1) + 1), int(y_axis_1) + 1, game_board, move_set)

    def rec_move_southwest(self, x_axis_1, y_axis_1, game_board, move_set):
        """
        Recursive method which takes the current x and y axes, the game board,
        and the move set list as parameters and returns an updated move set list
        containing the legal moves southwest-ward.
        """
        # CHECKS if square is out-of-bounds
        if x_axis_1 < "a" or y_axis_1 < 1:
            return move_set

        # IF current square is occupied by piece on opposite team
        if (game_board[x_axis_1][f"{y_axis_1}"] is not None and
                game_board[x_axis_1][f"{y_axis_1}"].get_color() != self._color):
            move_southwest = f"{x_axis_1}{y_axis_1}"
            move_set.append(move_southwest)
            return move_set

        # IF current square is occupied by piece on same team
        if (game_board[x_axis_1][f"{y_axis_1}"] is not None and
                game_board[x_axis_1][f"{y_axis_1}"].get_color() == self._color):
            return move_set

        # IF current square is empty
        if game_board[x_axis_1][f"{y_axis_1}"] is None:
            move_southwest = f"{x_axis_1}{y_axis_1}"
            move_set.append(move_southwest)
            self.rec_move_southwest(chr(ord(x_axis_1) - 1), int(y_axis_1) - 1, game_board, move_set)

    def rec_move_southeast(self, x_axis_1, y_axis_1, game_board, move_set):
        """
        Recursive method which takes the current x and y axes, the game board,
        and the move set list as parameters and returns an updated move set list
        containing the legal moves southeast-ward.
        """
        # CHECKS if square is out-of-bounds
        if x_axis_1 > "h" or y_axis_1 < 1:
            return move_set

        # IF current square is occupied by piece on opposite team
        if (game_board[x_axis_1][f"{y_axis_1}"] is not None and
                game_board[x_axis_1][f"{y_axis_1}"].get_color() != self._color):
            move_southeast = f"{x_axis_1}{y_axis_1}"
            move_set.append(move_southeast)
            return move_set

        # IF current square is occupied by piece on same team
        if (game_board[x_axis_1][f"{y_axis_1}"] is not None and
                game_board[x_axis_1][f"{y_axis_1}"].get_color() == self._color):
            return move_set

        # IF current square is empty
        if game_board[x_axis_1][f"{y_axis_1}"] is None:
            move_southeast = f"{x_axis_1}{y_axis_1}"
            move_set.append(move_southeast)
            self.rec_move_southeast(chr(ord(x_axis_1) + 1), int(y_axis_1) - 1, game_board, move_set)


class King(Piece):
    """
    Represents a king piece. Inherits from the Piece class.
    """

    def __init__(self, location):
        super().__init__(location)

    def move(self, square_1, square_2, game_board):
        """
        Takes as parameters two strings representing a source
        square and a destination square and determines whether
        the king piece can perform that move, returning True
        if so and False otherwise.
        """
        x_axis = square_1[0]
        y_axis = square_1[1]

        move_set = []

        # ADDS north move to move set if legal
        move_north = f"{x_axis}{int(y_axis) + 1}"
        if self._location[1] != "8":
            if game_board[move_north[0]][move_north[1]] is not None:
                if game_board[move_north[0]][move_north[1]].get_color() != self._color:
                    move_set.append(move_north)
            else:
                move_set.append(move_north)

        # ADDS northwest move to move set if legal
        move_northwest = f"{chr(ord(x_axis) - 1)}{int(y_axis) + 1}"
        if self._location[0] != "a" and self._location[1] != "8":
            if game_board[move_northwest[0]][move_northwest[1]] is not None:
                if game_board[move_northwest[0]][move_northwest[1]].get_color() != self._color:
                    move_set.append(move_northwest)
            else:
                move_set.append(move_northwest)

        # ADDS northeast move to move set if legal
        move_northeast = f"{chr(ord(x_axis) + 1)}{int(y_axis) + 1}"
        if self._location[0] != "h" and self._location[1] != "8":
            if game_board[move_northeast[0]][move_northeast[1]] is not None:
                if game_board[move_northeast[0]][move_northeast[1]].get_color() != self._color:
                    move_set.append(move_northeast)
            else:
                move_set.append(move_northeast)

        # ADDS west move to move set if legal
        move_west = f"{chr(ord(x_axis) - 1)}{y_axis}"
        if self._location[0] != "a":
            if game_board[move_west[0]][move_west[1]] is not None:
                if game_board[move_west[0]][move_west[1]].get_color() != self._color:
                    move_set.append(move_west)
            else:
                move_set.append(move_west)

        # ADDS east move to move set if legal
        move_east = f"{chr(ord(x_axis) + 1)}{y_axis}"
        if self._location[0] != "h":
            if game_board[move_east[0]][move_east[1]] is not None:
                if game_board[move_east[0]][move_east[1]].get_color() != self._color:
                    move_set.append(move_east)
            else:
                move_set.append(move_east)

        # ADDS southwest move to move set if legal
        move_southwest = f"{chr(ord(x_axis) - 1)}{int(y_axis) - 1}"
        if self._location[0] != "a" and self._location[1] != "1":
            if game_board[move_southwest[0]][move_southwest[1]] is not None:
                if game_board[move_southwest[0]][move_southwest[1]].get_color() != self._color:
                    move_set.append(move_southwest)
            else:
                move_set.append(move_southwest)

        # ADDS southeast move to move set if legal
        move_southeast = f"{chr(ord(x_axis) + 1)}{int(y_axis) - 1}"
        if self._location[0] != "h" and self._location[1] != "1":
            if game_board[move_southeast[0]][move_southeast[1]] is not None:
                if game_board[move_southeast[0]][move_southeast[1]].get_color() != self._color:
                    move_set.append(move_southeast)
            else:
                move_set.append(move_southeast)

        # ADDS south move to move set if legal
        move_south = f"{x_axis}{int(y_axis) - 1}"
        if self._location[1] != "1":
            if game_board[move_south[0]][move_south[1]] is not None:
                if game_board[move_south[0]][move_south[1]].get_color() != self._color:
                    move_set.append(move_south)
            else:
                move_set.append(move_south)

        # CHECKS if destination is in move set
        if square_2 in move_set:
            return True
        else:
            return False


class Queen(Piece):
    """
    Represents a queen piece. Inherits from the Piece class.
    """

    def __init__(self, location):
        super().__init__(location)

    def move(self, square_1, square_2, game_board):
        """
        Takes as parameters two strings representing a source
        square and a destination square and determines whether
        the queen piece can perform that move, returning True
        if so and False otherwise.
        """
        x_axis = square_1[0]
        y_axis = square_1[1]

        move_set = []

        # CHECKS if moving north is not out of range
        if y_axis != "8":
            self.rec_move_north(x_axis, int(y_axis) + 1, game_board, move_set)

        # CHECKS if moving south is not out of range
        if y_axis != "1":
            self.rec_move_south(x_axis, int(y_axis) - 1, game_board, move_set)

        # CHECKS if moving west is not out of range
        if x_axis != "a":
            self.rec_move_west(chr(ord(x_axis) - 1), y_axis, game_board, move_set)

        # CHECKS if moving east is not out of range
        if x_axis != "h":
            self.rec_move_east(chr(ord(x_axis) + 1), y_axis, game_board, move_set)

        # CHECKS if moving northwest is not out of range
        if x_axis != "a" and y_axis != "8":
            self.rec_move_northwest(chr(ord(x_axis) - 1), int(y_axis) + 1, game_board, move_set)

        # CHECKS if moving northeast is not out of range
        if x_axis != "h" and y_axis != "8":
            self.rec_move_northeast(chr(ord(x_axis) + 1), int(y_axis) + 1, game_board, move_set)

        # CHECKS if moving southwest is not out of range
        if x_axis != "a" and y_axis != "1":
            self.rec_move_southwest(chr(ord(x_axis) - 1), int(y_axis) - 1, game_board, move_set)

        # CHECKS if moving southeast is not out of range
        if x_axis != "h" and y_axis != "1":
            self.rec_move_southeast(chr(ord(x_axis) + 1), int(y_axis) - 1, game_board, move_set)

        # CHECKS if destination is in move set
        if square_2 in move_set:
            return True
        else:
            return False


class Rook(Piece):
    """
    Represents a rook piece. Inherits from the Piece class.
    """

    def __init__(self, location):
        super().__init__(location)

    def move(self, square_1, square_2, game_board):
        """
        Takes as parameters two strings representing a source
        square and a destination square and determines whether
        the rook piece can perform that move, returning True
        if so and False otherwise.
        """
        x_axis = square_1[0]
        y_axis = square_1[1]

        move_set = []

        # CHECKS if moving north is not out of range
        if y_axis != "8":
            self.rec_move_north(x_axis, int(y_axis) + 1, game_board, move_set)

        # CHECKS if moving south is not out of range
        if y_axis != "1":
            self.rec_move_south(x_axis, int(y_axis) - 1, game_board, move_set)

        # CHECKS if moving west is not out of range
        if x_axis != "a":
            self.rec_move_west(chr(ord(x_axis) - 1), y_axis, game_board, move_set)

        # CHECKS if moving east is not out of range
        if x_axis != "h":
            self.rec_move_east(chr(ord(x_axis) + 1), y_axis, game_board, move_set)

        # CHECKS if destination is in move set
        if square_2 in move_set:
            return True
        else:
            return False


class Bishop(Piece):
    """
    Represents a bishop piece. Inherits from the Piece class.
    """

    def __init__(self, location):
        super().__init__(location)

    def move(self, square_1, square_2, game_board):
        """
        Takes as parameters two strings representing a source
        square and a destination square and determines whether
        the bishop piece can perform that move, returning True
        if so and False otherwise.
        """
        x_axis = square_1[0]
        y_axis = square_1[1]

        move_set = []

        # CHECKS if moving northwest is not out of range
        if x_axis != "a" and y_axis != "8":
            self.rec_move_northwest(chr(ord(x_axis) - 1), int(y_axis) + 1, game_board, move_set)

        # CHECKS if moving northeast is not out of range
        if x_axis != "h" and y_axis != "8":
            self.rec_move_northeast(chr(ord(x_axis) + 1), int(y_axis) + 1, game_board, move_set)

        # CHECKS if moving southwest is not out of range
        if x_axis != "a" and y_axis != "1":
            self.rec_move_southwest(chr(ord(x_axis) - 1), int(y_axis) - 1, game_board, move_set)

        # CHECKS if moving southeast is not out of range
        if x_axis != "h" and y_axis != "1":
            self.rec_move_southeast(chr(ord(x_axis) + 1), int(y_axis) - 1, game_board, move_set)

        if square_2 in move_set:
            return True
        else:
            return False


class Knight(Piece):
    """
    Represents a knight piece. Inherits from the Piece class.
    """

    def __init__(self, location):
        super().__init__(location)

    def move(self, square_1, square_2, game_board):
        """
        Takes as parameters two strings representing a source
        square and a destination square and determines whether
        the knight piece can perform that move, returning True
        if so and False otherwise.
        """
        x_axis = square_1[0]
        y_axis = square_1[1]

        move_set = []

        # ADDS north-northwest move to move set if legal
        move_nnw = f"{chr(ord(x_axis) - 1)}{int(y_axis) + 2}"
        if self._location[0] != "a" and self._location[1] < "7":
            if game_board[move_nnw[0]][move_nnw[1]] is not None:
                if game_board[move_nnw[0]][move_nnw[1]].get_color() != self._color:
                    move_set.append(move_nnw)
            else:
                move_set.append(move_nnw)

        # ADDS northwest move to move set if legal
        move_northwest = f"{chr(ord(x_axis) - 2)}{int(y_axis) + 1}"
        if self._location[0] > "b" and self._location[1] != "8":
            if game_board[move_northwest[0]][move_northwest[1]] is not None:
                if game_board[move_northwest[0]][move_northwest[1]].get_color() != self._color:
                    move_set.append(move_northwest)
            else:
                move_set.append(move_northwest)

        # ADDS north-northeast move to move set if legal
        move_nne = f"{chr(ord(x_axis) + 1)}{int(y_axis) + 2}"
        if self._location[0] != "h" and self._location[1] < "7":
            if game_board[move_nne[0]][move_nne[1]] is not None:
                if game_board[move_nne[0]][move_nne[1]].get_color() != self._color:
                    move_set.append(move_nne)
            else:
                move_set.append(move_nne)

        # ADDS northeast move to move set if legal
        move_northeast = f"{chr(ord(x_axis) + 2)}{int(y_axis) + 1}"
        if self._location[0] < "g" and self._location[1] != "8":
            if game_board[move_northeast[0]][move_northeast[1]] is not None:
                if game_board[move_northeast[0]][move_northeast[1]].get_color() != self._color:
                    move_set.append(move_northeast)
            else:
                move_set.append(move_northeast)

        # ADDS south-southwest move to move set if legal
        move_ssw = f"{chr(ord(x_axis) - 1)}{int(y_axis) - 2}"
        if self._location[0] != "a" and self._location[1] > "2":
            if game_board[move_ssw[0]][move_ssw[1]] is not None:
                if game_board[move_ssw[0]][move_ssw[1]].get_color() != self._color:
                    move_set.append(move_ssw)
            else:
                move_set.append(move_ssw)

        # ADDS southwest move to move set if legal
        move_southwest = f"{chr(ord(x_axis) - 2)}{int(y_axis) - 1}"
        if self._location[0] > "b" and self._location[1] != "1":
            if game_board[move_southwest[0]][move_southwest[1]] is not None:
                if game_board[move_southwest[0]][move_southwest[1]].get_color() != self._color:
                    move_set.append(move_southwest)
            else:
                move_set.append(move_southwest)

        # ADDS south-southeast move to move set if legal
        move_sse = f"{chr(ord(x_axis) + 1)}{int(y_axis) - 2}"
        if self._location[0] != "h" and self._location[1] > "2":
            if game_board[move_sse[0]][move_sse[1]] is not None:
                if game_board[move_sse[0]][move_sse[1]].get_color() != self._color:
                    move_set.append(move_sse)
            else:
                move_set.append(move_sse)

        # ADDS southeast move to move set if legal
        move_southeast = f"{chr(ord(x_axis) + 2)}{int(y_axis) - 1}"
        if self._location[0] < "g" and self._location[1] != "1":
            if game_board[move_southeast[0]][move_southeast[1]] is not None:
                if game_board[move_southeast[0]][move_southeast[1]].get_color() != self._color:
                    move_set.append(move_southeast)
            else:
                move_set.append(move_southeast)

        # CHECKS if destination is in move set
        if square_2 in move_set:
            return True
        else:
            return False


class WhiteKing(King):
    """
    Represents a king piece on the white team.
    Inherits from King class.
    """

    def __init__(self, location):
        super().__init__(location)

        self._symbol = "♔"
        self._color = "WHITE"


class WhiteQueen(Queen):
    """
    Represents a queen piece on the white team.
    Inherits from Queen class.
    """

    def __init__(self, location):
        super().__init__(location)

        self._symbol = "♕"
        self._color = "WHITE"


class WhiteRook(Rook):
    """
    Represents a rook piece on the white team.
    Inherits from Piece class.
    """

    def __init__(self, location):
        super().__init__(location)

        self._symbol = "♖"
        self._color = "WHITE"


class WhiteBishop(Bishop):
    """
    Represents a bishop piece on the white team.
    Inherits from Piece class.
    """

    def __init__(self, location):
        super().__init__(location)

        self._symbol = "♗"
        self._color = "WHITE"


class WhiteKnight(Knight):
    """
    Represents a knight piece on the white team.
    Inherits from Knight class.
    """

    def __init__(self, location):
        super().__init__(location)

        self._symbol = "♘"
        self._color = "WHITE"


class WhitePawn(Piece):
    """
    Represents a pawn piece on the white team.
    Inherits from Piece class.
    """

    def __init__(self, location):
        super().__init__(location)

        self._symbol = "♙"
        self._color = "WHITE"

    def move(self, square_1, square_2, game_board):
        """
        Takes as parameters two strings representing a source
        square and a destination square and determines whether
        the white pawn piece can perform that move, returning True
        if so and False otherwise.
        """
        x_axis = square_1[0]
        y_axis = square_1[1]

        move_set = []

        # ADDS north move to move set if legal
        move_up = f"{x_axis}{int(y_axis) + 1}"
        if game_board[move_up[0]][move_up[1]] is None:
            move_set.append(move_up)

        # ADDS northwest move to move set if legal
        move_diag_1 = f"{chr(ord(x_axis) - 1)}{int(y_axis) + 1}"
        if self._location[0] != "a" and self._location[1] != "8":
            if game_board[move_diag_1[0]][move_diag_1[1]] is not None:
                if game_board[move_diag_1[0]][move_diag_1[1]].get_color() != self._color:
                    move_set.append(move_diag_1)

        # ADDS northeast move to move set if legal
        move_diag_2 = f"{chr(ord(x_axis) + 1)}{int(y_axis) + 1}"
        if self._location[0] != "h" and self._location[1] != "8":
            if game_board[move_diag_2[0]][move_diag_2[1]] is not None:
                if game_board[move_diag_2[0]][move_diag_2[1]].get_color() != self._color:
                    move_set.append(move_diag_2)

        # ADDS double northward move to move set if legal
        move_two = f"{x_axis}{int(y_axis) + 2}"
        if self._location[1] == "2":
            if game_board[move_two[0]][move_two[1]] is None:
                move_set.append(move_two)

        # CHECKS if destination is in move set
        if square_2 in move_set:
            return True
        else:
            return False


class WhiteFalcon(Piece):
    """
    Represents a falcon piece on the white team.
    Inherits from Piece class.
    """

    def __init__(self, location):
        super().__init__(location)

        self._symbol = 'F'
        self._color = "WHITE"

    def move(self, square_1, square_2, game_board):
        """
        Takes as parameters two strings representing a source
        square and a destination square and determines whether
        the white falcon piece can perform that move, returning True
        if so and False otherwise.
        """
        x_axis = square_1[0]
        y_axis = square_1[1]

        move_set = []

        # CHECKS if moving northwest is not out of range
        if x_axis != "a" and y_axis != "8":
            self.rec_move_northwest(chr(ord(x_axis) - 1), int(y_axis) + 1, game_board, move_set)

        # CHECKS if moving northeast is not out of range
        if x_axis != "h" and y_axis != "8":
            self.rec_move_northeast(chr(ord(x_axis) + 1), int(y_axis) + 1, game_board, move_set)

        # CHECKS if moving south is not out of range
        if y_axis != "1":
            self.rec_move_south(x_axis, int(y_axis) - 1, game_board, move_set)

        # CHECKS if destination is in move set
        if square_2 in move_set:
            return True
        else:
            return False


class WhiteHunter(Piece):
    """
    Represents a hunter piece on the white team.
    Inherits from Piece class.
    """

    def __init__(self, location):
        super().__init__(location)

        self._symbol = 'H'
        self._color = "WHITE"

    def move(self, square_1, square_2, game_board):
        """
        Takes as parameters two strings representing a source
        square and a destination square and determines whether
        the white hunter piece can perform that move, returning True
        if so and False otherwise.
        """
        x_axis = square_1[0]
        y_axis = square_1[1]

        move_set = []

        # CHECKS if moving northward is not out of range
        if y_axis != "8":
            self.rec_move_north(x_axis, int(y_axis) + 1, game_board, move_set)

        # CHECKS if moving southwest-ward is not out of range
        if x_axis != "a" and y_axis != "1":
            self.rec_move_southwest(chr(ord(x_axis) - 1), int(y_axis) - 1, game_board, move_set)

        # CHECKS if moving southeast-ward is not out of range
        if x_axis != "h" and y_axis != "1":
            self.rec_move_southeast(chr(ord(x_axis) + 1), int(y_axis) - 1, game_board, move_set)

        # CHECKS if destination is in move set
        if square_2 in move_set:
            return True
        else:
            return False


class BlackKing(King):
    """
    Represents a king piece on the black team.
    Inherits from King class.
    """

    def __init__(self, location):
        super().__init__(location)

        self._symbol = "♚"
        self._color = "BLACK"


class BlackQueen(Queen):
    """
    Represents a queen piece on the black team.
    Inherits from Queen class.
    """

    def __init__(self, location):
        super().__init__(location)

        self._symbol = "♛"
        self._color = "BLACK"


class BlackRook(Rook):
    """
    Represents a rook piece on the black team.
    Inherits from Piece class.
    """

    def __init__(self, location):
        super().__init__(location)

        self._symbol = "♜"
        self._color = "BLACK"


class BlackBishop(Bishop):
    """
    Represents a bishop piece on the black team.
    Inherits from Piece class.
    """

    def __init__(self, location):
        super().__init__(location)

        self._symbol = "♝"
        self._color = "BLACK"


class BlackKnight(Knight):
    """
    Represents a knight piece on the black team.
    Inherits from Knight class.
    """

    def __init__(self, location):
        super().__init__(location)

        self._symbol = "♞"
        self._color = "BLACK"


class BlackPawn(Piece):
    """
    Represents a pawn piece on the black team.
    Inherits from Pawn class.
    """

    def __init__(self, location):
        super().__init__(location)

        self._symbol = "♟︎"
        self._color = "BLACK"

    def move(self, square_1, square_2, game_board):
        """
        Takes as parameters two strings representing a source
        square and a destination square and determines whether
        the black pawn piece can perform that move, returning True
        if so and False otherwise.
        """
        x_axis = square_1[0]
        y_axis = square_1[1]

        move_set = []

        # ADDS south move to move set if legal
        move_up = f"{x_axis}{int(y_axis) - 1}"
        if game_board[move_up[0]][move_up[1]] is None:
            move_set.append(move_up)

        # ADDS southeast move to move set if legal
        move_diag_1 = f"{chr(ord(x_axis) + 1)}{int(y_axis) - 1}"
        if self._location[0] != "h":
            if game_board[move_diag_1[0]][move_diag_1[1]] is not None:
                if game_board[move_diag_1[0]][move_diag_1[1]].get_color() != self._color:
                    move_set.append(move_diag_1)

        # ADDS southwest move to move set if legal
        move_diag_2 = f"{chr(ord(x_axis) - 1)}{int(y_axis) - 1}"
        if self._location[0] != "a":
            if game_board[move_diag_2[0]][move_diag_2[1]] is not None:
                if game_board[move_diag_2[0]][move_diag_2[1]].get_color() != self._color:
                    move_set.append(move_diag_2)

        # ADDS double southward move to move set if legal
        move_two = f"{x_axis}{int(y_axis) - 2}"
        if self._location[1] == "7":
            if game_board[move_two[0]][move_two[1]] is None:
                move_set.append(move_two)

        # CHECKS if destination is in move set
        if square_2 in move_set:
            return True
        else:
            return False


class BlackFalcon(Piece):
    """
    Represents a falcon piece on the black team.
    Inherits from Piece class.
    """

    def __init__(self, location):
        super().__init__(location)

        self._symbol = "f"
        self._color = "BLACK"

    def move(self, square_1, square_2, game_board):
        """
        Takes as parameters two strings representing a source
        square and a destination square and determines whether
        the black falcon piece can perform that move, returning True
        if so and False otherwise.
        """
        x_axis = square_1[0]
        y_axis = square_1[1]

        move_set = []

        # CHECKS if moving north is not out of range
        if y_axis != "8":
            self.rec_move_north(x_axis, int(y_axis) + 1, game_board, move_set)

        # CHECKS if moving southwest is not out of range
        if x_axis != "a" and y_axis != "1":
            self.rec_move_southwest(chr(ord(x_axis) - 1), int(y_axis) - 1, game_board, move_set)

        # CHECKS if moving southeast is not out of range
        if x_axis != "h" and y_axis != "1":
            self.rec_move_southeast(chr(ord(x_axis) + 1), int(y_axis) - 1, game_board, move_set)

        # CHECKS if destination is in move set
        if square_2 in move_set:
            return True
        else:
            return False


class BlackHunter(Piece):
    """
    Represents a hunter piece on the black team.
    Inherits from Piece class.
    """

    def __init__(self, location):
        super().__init__(location)

        self._symbol = "h"
        self._color = "BLACK"

    def move(self, square_1, square_2, game_board):
        """
        Takes as parameters two strings representing a source
        square and a destination square and determines whether
        the black hunter piece can perform that move, returning True
        if so and False otherwise.
        """
        x_axis = square_1[0]
        y_axis = square_1[1]

        move_set = []

        # CHECKS if moving northwest is not out of range
        if x_axis != "a" and y_axis != "8":
            self.rec_move_northwest(chr(ord(x_axis) - 1), int(y_axis) + 1, game_board, move_set)

        # CHECKS if moving northeast is not out of range
        if x_axis != "h" and y_axis != "8":
            self.rec_move_northeast(chr(ord(x_axis) + 1), int(y_axis) + 1, game_board, move_set)

        # CHECKS if moving south is not out of range 
        if y_axis != "1":
            self.rec_move_south(x_axis, int(y_axis) - 1, game_board, move_set)

        # CHECKS if destination is in move set
        if square_2 in move_set:
            return True
        else:
            return False


def main():
    game = ChessVar()

    game.make_move('a2', 'a4')
    game.show_board()

if __name__ == '__main__':
    main()

# DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
# 1. Initializing the ChessVar class
# Initialize the game status to 'UNFINISHED'
# Initialize the turn count to 0
# Initialize the chess board and off-board to an empty dictionary
# Call the start_game method which initializes the chess board dictionary's keys
# Call the set_pieces method which sets all the game pieces to their starting positions
# Set turn count to 1

# 2. Keeping track of turn order
# Once turn count is set to 1, the make_move method can be called
# When the make_move method is called, the turn counter is checked for an even or odd value
# If the value is odd, only pieces with a "WHITE" color data member can be moved.
# If the value is even, only pieces with a "BLACK" color data member can be moved.
# After every call to the make_move method, the turn counter is incremented by 1

# 3. Keeping track of the current board position
# A piece's location data member is set to the square it is initialized in
# A piece's location data member is set to the destination square
# when it is moved using the make_move method.
# The show_Board method can be called to return a visual representation of the board.

# 4. Determining if a regular move is valid
# The make_move method calls the move method of the piece object in the source square
# The piece's move method generates a list of legal destination squares reachable
# from the source square.
# Iterate through the list to check if any of the destinations matches the user input.
# If there is a match, the move is legal and the make_move method can proceed.
# If there is no match, the move is illegal and the make_move method will return False.

# 5. Determining if a fairy piece entering move is valid
# The enter_fairy_piece method calls the captured_list method
# Check if the team has had a major piece captured in the list of captured pieces to allow
# the first piece to be placed. Checks to make sure at least two have been captured to allow
# the other to be placed.
# If both are true, the fairy piece entering move is valid and the enter_fairy_method proceeds
# If either is not true, the fairy piece entering move is invalid
# and the enter_fairy_method returns False.

# 6. Determining the current state of the game
# The get_game_state method calls the captured_list method
# Check if the last piece captured was a king piece object
# If so, check king piece object's color data member
# If king piece object's color data member is "WHITE", game status is "BLACK_WON"
# If king piece object's color data member is "BLACK", game status is "WHITE_WON"
# If the last piece captureD was not a king piece object, game status is "UNFINISHED"
