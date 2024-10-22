# chess_game.py
class ChessGame:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

    def start(self):
        while not self.is_game_over():
            print(f"Current turn: {self.current_player.name}")
            self.board.print_board()
            move = self.current_player.get_move()
            
            if self.board.move_piece(move.from_pos, move.to_pos, self.current_player.color):
                self.switch_turn()
            else:
                print("Invalid move. Try again.")

        print(f"Game over! Winner: {(self.player1.name if self.current_player == self.player2 else self.player2.name)}")

    def is_game_over(self):
        # TODO: Implement checkmate logic here
        pass

    def switch_turn(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
