# Chess Variant Implementation

An implementation of a chess variant featuring traditional chess pieces enhanced with unique fairy pieces (Hunter and Falcon). This project demonstrates object-oriented programming principles, recursive algorithms, and game state management in Python.

## Table of Contents

- [Overview](#overview)
- [Example Output](#example-output)
- [Features](#features)
- [Game Rules](#game-rules)
- [Class Architecture](#class-architecture)
- [Installation & Setup](#installation--setup)
- [Usage Examples](#usage-examples)
- [Testing](#testing)
- [Game Mechanics](#game-mechanics)
- [Learning Outcomes](#learning-outcomes)
- [References](#references)

## Overview

This project implements a chess variant that extends traditional chess with two unique fairy pieces:

- **Hunter (H/h)**: Moves like a combination of rook and bishop in specific directions
- **Falcon (F/f)**: Moves like a combination of bishop and rook in specific directions

The implementation features a complete game engine with move validation, turn management, piece capture tracking, and visual board representation. The game ends when either king is captured, following standard chess victory conditions.

## Example Output

```
Initial Board:
[['OFF BOARD'], ['h'], ['f']]
[['8'], ['♜'], ['♞'], ['♝'], ['♛'], ['♚'], ['♝'], ['♞'], ['♜']]
[['7'], ['♟︎'], ['♟︎'], ['♟︎'], ['♟︎'], ['♟︎'], ['♟︎'], ['♟︎'], ['♟︎']]
[['6'], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' ']]
[['5'], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' ']]
[['4'], ['♙'], [' '], [' '], [' '], [' '], [' '], [' '], [' ']]
[['3'], [' '], [' '], [' '], [' '], [' '], [' '], [' '], [' ']]
[['2'], [' '], ['♙'], ['♙'], ['♙'], ['♙'], ['♙'], ['♙'], ['♙']]
[['1'], ['♖'], ['♘'], ['♗'], ['♕'], ['♔'], ['♗'], ['♘'], ['♖']]
[[' '], ['a'], ['b'], ['c'], ['d'], ['e'], ['f'], ['g'], ['h']]
[['OFF BOARD'], ['H'], ['F']]
```

## Features

### Core Game Features
- **Complete Chess Engine**: Full implementation of traditional chess rules
- **Fairy Piece Integration**: Two unique piece types with custom movement patterns
- **Turn Management**: Automatic alternating turns between white and black players
- **Move Validation**: Comprehensive legal move checking for all piece types
- **Capture Tracking**: Detailed tracking of captured pieces and game state
- **Visual Board**: ASCII-based board representation with Unicode chess symbols
- **Game State Management**: Real-time tracking of game status (UNFINISHED, WHITE_WON, BLACK_WON)

### Technical Features
- **Object-Oriented Design**: Clean inheritance hierarchy with base Piece class
- **Recursive Algorithms**: Efficient move calculation using recursive methods
- **Polymorphism**: Unified interface for different piece types
- **Data Structures**: Dictionary-based board representation for O(1) access
- **Input Validation**: Robust error handling for invalid moves and inputs

## Game Rules

### Traditional Chess Pieces
- **King**: Moves one square in any direction
- **Queen**: Combines rook and bishop movement
- **Rook**: Moves horizontally and vertically
- **Bishop**: Moves diagonally
- **Knight**: Moves in L-shaped patterns
- **Pawn**: Moves forward, captures diagonally, special double-move from starting position

### Fairy Pieces
- **Hunter (H/h)**:
  - White Hunter: Moves north, southwest, and southeast (like rook + bishop)
  - Black Hunter: Moves south, northwest, and northeast (like rook + bishop)
- **Falcon (F/f)**:
  - White Falcon: Moves northwest, northeast, and south (like bishop + rook)
  - Black Falcon: Moves southwest, southeast, and north (like bishop + rook)

### Fairy Piece Entry Rules
- Fairy pieces start off-board and can only enter when:
  - At least one major piece (Queen, Rook, Bishop, Knight) has been captured
  - For the second fairy piece: at least two major pieces must be captured
- Fairy pieces can only enter on the player's side of the board (rows 1-2 for white, rows 7-8 for black)

## Class Architecture

### Main Game Class
```python
class ChessVar:
    def __init__(self):
        self._game_state = 'UNFINISHED'
        self._turn_count = 0
        self._board = {}
        self._off_board = {}
        self._captured = []
```

### Piece Hierarchy
```python
class Piece:                    # Base piece class
    def move(self, from_square, to_square, game_board)
    def rec_move_north(self, x, y, board, moves)    # Recursive movement methods
    # ... other directional movement methods

class King(Piece):              # Traditional pieces
class Queen(Piece):
class Rook(Piece):
class Bishop(Piece):
class Knight(Piece):
class WhitePawn(Piece):         # Team-specific pieces
class BlackPawn(Piece):
class WhiteHunter(Piece):       # Fairy pieces
class BlackHunter(Piece):
class WhiteFalcon(Piece):
class BlackFalcon(Piece):
```

## Installation & Setup

### Prerequisites
- Python 3.7+
- No external dependencies required

### Setup Instructions

1. **Clone or download** the project files
2. **Navigate** to the Chess Variant directory:
   ```bash
   cd "Chess Variant"
   ```

3. **Run the game**:
   ```bash
   python ChessVar.py
   ```

## Usage Examples

### Basic Game Initialization

```python
from ChessVar import ChessVar

# Create a new game
game = ChessVar()

# Display the initial board
game.show_board()
```

### Making Moves

```python
# Make a legal move (white pawn)
success = game.make_move('a2', 'a4')
print(f"Move successful: {success}")

# Make another move (black pawn)
success = game.make_move('e7', 'e5')
print(f"Move successful: {success}")

# Display updated board
game.show_board()
```

### Fairy Piece Entry

```python
# After capturing pieces, enter fairy pieces
# Enter white hunter (requires captured pieces)
success = game.enter_fairy_piece('H', 'b1')
print(f"Fairy piece entry: {success}")

# Enter black falcon
success = game.enter_fairy_piece('f', 'f8')
print(f"Fairy piece entry: {success}")
```

### Game State Management

```python
# Check current game state
state = game.get_game_state()
print(f"Game state: {state}")  # UNFINISHED, WHITE_WON, or BLACK_WON

# Check turn count
turn = game.get_turn_count()
print(f"Current turn: {turn}")

# View captured pieces
captured = game.get_captured_list()
print(f"Captured pieces: {captured}")
```

### Complete Game Example

```python
def play_sample_game():
    game = ChessVar()
    
    # Display initial board
    print("Initial Board:")
    game.show_board()
    
    # Make some moves
    game.make_move('e2', 'e4')  # White pawn
    game.make_move('e7', 'e5')  # Black pawn
    game.make_move('g1', 'f3')  # White knight
    game.make_move('b8', 'c6')  # Black knight
    
    print("\nAfter opening moves:")
    game.show_board()
    
    # Check game state
    print(f"\nGame state: {game.get_game_state()}")
    print(f"Turn: {game.get_turn_count()}")

if __name__ == "__main__":
    play_sample_game()
```

## Testing

### Running the Game

```bash
# Run the main game with sample moves
python ChessVar.py
```

### Test Coverage

The implementation includes comprehensive testing through:

- **Move Validation**: All piece types tested for legal/illegal moves
- **Turn Management**: Proper alternating turns between players
- **Fairy Piece Logic**: Entry conditions and movement validation
- **Game State**: Win condition detection and state transitions
- **Edge Cases**: Boundary conditions, invalid inputs, and error handling

### Manual Testing Scenarios

1. **Basic Movement**: Test each piece type's movement patterns
2. **Capture Logic**: Verify piece capture and removal
3. **Turn Alternation**: Ensure proper turn management
4. **Fairy Piece Entry**: Test entry conditions and restrictions
5. **Win Conditions**: Test king capture scenarios
6. **Invalid Moves**: Verify rejection of illegal moves

## Game Mechanics

### Board Representation
- **Coordinate System**: Algebraic notation (a1-h8)
- **Data Structure**: Nested dictionaries for O(1) square access
- **Visual Display**: Unicode chess symbols with ASCII formatting

### Move Validation Process
1. **Input Validation**: Check square format and bounds
2. **Piece Verification**: Ensure piece exists and belongs to current player
3. **Legal Move Check**: Use piece-specific move method
4. **Execution**: Update board state and piece location
5. **State Update**: Increment turn counter and check win conditions

### Fairy Piece Mechanics
- **Off-Board Storage**: Separate tracking of fairy pieces
- **Entry Conditions**: Based on captured piece count
- **Movement Patterns**: Unique directional combinations
- **Team Restrictions**: Different movement for white/black pieces

## Learning Outcomes

This project demonstrates:

- **Object-Oriented Programming**: Inheritance, polymorphism, and encapsulation
- **Recursive Algorithms**: Efficient move calculation and board traversal
- **Game Development**: State management and rule implementation
- **Data Structures**: Dictionary-based board representation
- **Algorithm Design**: Move validation and game logic
- **Code Organization**: Modular design with clear separation of concerns
- **Error Handling**: Robust input validation and edge case management

## References

- [Chess Rules - Wikipedia](https://en.wikipedia.org/wiki/Rules_of_chess)
- [Chess Variants - Wikipedia](https://en.wikipedia.org/wiki/Chess_variant)
- [Object-Oriented Programming in Python](https://docs.python.org/3/tutorial/classes.html)
- [Recursive Algorithms - GeeksforGeeks](https://www.geeksforgeeks.org/recursion/)

---

**Author**: Josue Bustamante  
**Course**: CS261 - Data Structures  
**Institution**: Oregon State University  
**Date**: March 2024
