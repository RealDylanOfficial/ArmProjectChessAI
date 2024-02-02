import chess
import chess.polyglot
from . import heuristics

from . import tables
from . import util


class AI_AlphaBeta: # Class for calculating the best move
    INFINITE = 10000000
    PIECE_VALUES = [0, 100, 300, 330, 500, 900, INFINITE]
    boards_evaluated = 0
    # piece values for second evaluation solution:
    piece_values = {"p":1, "k":10, "b":5, "r":5, "q":8, "n":4}

    def __init__(self, colour=None):
        pass

    def get_move(self, board, depth):
        best_eval = -self.INFINITE
        self.boards_evaluated = 0

        moves = list(board.legal_moves)
 
        best_move = None

        for move in board.legal_moves:
            board.push(move)

            eval = self.alphabeta(board, depth-1, -self.INFINITE, self.INFINITE)

            if (eval > best_eval):
                best_eval = eval
                best_move = move

            board.pop()

        return best_move
    
    def minimax(self, depth, board, is_maximizing):
        pass

    # def alphabeta(self, board, depth, alpha, beta):
    #     if depth == 0:
    #         self.boards_evaluated += 1
    #         return self.evaluate3(board)

    #     moves = list(board.legal_moves)
    #     moves = self.order_moves(board, moves)

    #     if (len(moves) == 0):
    #         return 0

    #     for move in moves:
    #         board.push(move)
    #         eval = -self.alphabeta(board, depth-1, -beta, -alpha)
    #         board.pop()

    #         if (eval >= beta):
    #             return beta
    #         if (eval > alpha):
    #             alpha = eval

    #     return eval
    
    def alphabeta(self, board: chess.Board, depth, alpha, beta):
        if depth == 0:
            return self.evaluate3(board)

        moves = list(board.legal_moves)

        if len(moves) == 0:
            return self.evaluate3(board)

        if depth % 2 == 0:  # maximising
            eval = float("-inf")
            for move in moves:
                board.push(move)
                eval = max(eval, self.alphabeta(board, depth-1, beta, alpha))  # Fix function name
                board.pop()

                if eval > beta:
                    break
                
                alpha = max(alpha, eval)
            return eval
        else:   # minimising
            eval = float("inf")
            for move in moves:
                board.push(move)
                eval = min(eval, self.alphabeta(board, depth-1, beta, alpha))  # Fix function name
                board.pop()

                if eval < alpha:
                    break
                
                beta = min(beta, eval)
            


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
    
    def evaluate2(self, board: chess.Board):
        value = 0
        for i in range(64):
            piece = board.piece_at(i)
            if piece is not None:
                if piece.color == board.turn:
                    symbol = piece.symbol().lower()
                    value += self.piece_values[symbol]
                else:
                    symbol = piece.symbol().lower()
                    value -= self.piece_values[symbol]
        if board.is_checkmate() and board.outcome().winner != board.turn:
            print("test1")
            return 100000
        if board.is_game_over() and board.outcome().winner == board.turn or board.is_repetition():
            print("test2")
            return -100000
        
                    
        return value
    
    def evaluate3(self, board: chess.Board):
        score = 0
        score += heuristics.material(board, 100)
        score += heuristics.piece_moves(board, 50)
        score += heuristics.pawn_structure(board, 1)
        score += heuristics.in_check(board, 1)

        return score
        

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
