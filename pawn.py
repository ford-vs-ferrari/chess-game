# pawn.py
class Pawn(Piece):
    def is_valid_move(self, new_position, board):
        # TODO: Implement pawn's movement and capture logic
        pass

    def get_symbol(self):
        return 'P' if self.color == 'WHITE' else 'p'
