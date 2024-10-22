# board.py
class Board:
    def __init__(self):
        self.squares = [[None for _ in range(8)] for _ in range(8)]
        self.initialize_board()

    def initialize_board(self):
        # Place Pawns
        for i in range(8):
            self.squares[1][i] = Pawn('WHITE', Position(1, i))
            self.squares[6][i] = Pawn('BLACK', Position(6, i))

        # TODO: Add other pieces (Rooks, Knights, Bishops, Queens, Kings)

    def move_piece(self, from_pos, to_pos, player_color):
        piece = self.get_piece_at(from_pos)
        if piece and piece.color == player_color and piece.is_valid_move(to_pos, self):
            # TODO: Check if the move is valid (path clear, valid capture, etc.)
            self.squares[to_pos.row][to_pos.col] = piece
            self.squares[from_pos.row][from_pos.col] = None
            piece.position = to_pos
            return True
        return False

    def get_piece_at(self, position):
        return self.squares[position.row][position.col]

    def print_board(self):
        for row in self.squares:
            print(' '.join([piece.get_symbol() if piece else '.' for piece in row]))

    def is_king_in_checkmate(self, color):
        # TODO: Implement checkmate detection
        pass
