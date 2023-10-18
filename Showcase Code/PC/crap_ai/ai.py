import chess
import chess.polyglot

from . import tables
from . import util

# REMOVE THIS: This is doing alpha-beta pruning to make the best decision
# Alpha-beta pruning is 
class AI_AlphaBeta: # Class for calculating the best move
    INFINITE = 10000000 
    PIECE_VALUES = [0, 100, 300, 330, 500, 900, INFINITE] #Sets out numerical "value" to pieces.
    boards_evaluated = 0 # Maybe the number of trials the ai has completed   CHECK THIS AGAIN

    def __init__(self):  # Classes need to be initialized. This class is used for a set of functions.
        pass #"pass" is run so there is no error if the function is empty.

    def get_move(self, board, depth): # 
        best_eval = -self.INFINITE
        self.boards_evaluated = 0

        moves = list(board.legal_moves)
        # print(moves)
        # moves = self.order_moves(board, moves)
        best_move = None

        for move in board.legal_moves:
            board.push(move)

            eval = -self.alphabeta(board, depth-1, -self.INFINITE, self.INFINITE)

            if (eval > best_eval):
                best_eval = eval
                best_move = move

            board.pop()

        return best_move

    def alphabeta(self, board, depth, alpha, beta):
        if depth == 0:
            self.boards_evaluated += 1
            return self.evaluate(board)

        moves = list(board.legal_moves)
        moves = self.order_moves(board, moves)

        if (len(moves) == 0):
            return 0

        for move in moves:
            board.push(move)
            eval = -self.alphabeta(board, depth-1, -beta, -alpha)
            board.pop()

            if (eval >= beta):
                return beta
            if (eval > alpha):
                alpha = eval

        return eval

    def evaluate(self, board):
        value = 0

        for i in range(64):
            piece = board.piece_at(i)
            if piece is not None:
                if piece.color == board.turn:
                    value += self.PIECE_VALUES[piece.piece_type]
                    value += tables.PIECE_TABLE[piece.piece_type][int(i/8)][i%8]
                else:
                    value -= self.PIECE_VALUES[piece.piece_type]
                    value -= tables.PIECE_TABLE[piece.piece_type][int(i/8)][i%8]

        return value

    def test_openings(self, board):
        with chess.polyglot.open_reader("data/polyglot/performance.bin") as reader:
            for entry in reader.find_all(board):
                print(entry.move, entry.weight, entry.learn)

    def order_moves(self, board, moves):
        move_scores = []

        for move in moves:
            score = 0

            if board.is_capture(move) and board.piece_at(move.to_square) is not None:
                score += 10 * self.PIECE_VALUES[board.piece_at(move.to_square).piece_type] - self.PIECE_VALUES[board.piece_at(move.from_square).piece_type]

            move_scores.append(score)

        return util.bubble_sort(moves, move_scores)
