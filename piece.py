# piece.py
class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def is_valid_move(self, new_position, board):
        # TODO: Implement logic to validate move for each piece
        pass

    def get_symbol(self):
        # TODO: Return piece symbol (e.g., P for pawn, K for king, etc.)
        pass
