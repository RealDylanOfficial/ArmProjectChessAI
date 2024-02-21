import os
import chess
import chess.polyglot
from . import heuristics

# from . import tables
from . import util


class AI_AlphaBeta: # Class for calculating the best move
    INFINITE = 10000000
    PIECE_VALUES = [0, 100, 300, 330, 500, 900, INFINITE]
    # piece values for second evaluation solution:
    piece_values = {"p":1, "k":10, "b":5, "r":5, "q":8, "n":4}

    def __init__(self, colour=None):
        self.cached = {}
        try:
            script_directory = os.path.dirname(os.path.abspath(__file__))
            
            with open(os.path.join(script_directory, "cached.txt"), "r") as file:
                file_contents = file.read().splitlines()
                for line in file_contents:
                    input, output = line.split(":")
                    self.cached[input] = output
        except FileNotFoundError:
            print("File 'cached.txt' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_move(self, board: chess.Board, depth):
        
        best_eval = -self.INFINITE

        moves = list(board.legal_moves)
 
        best_move = None

        for move in board.legal_moves:
            board.push(move)

            eval = self.alphabeta(board, depth, -self.INFINITE, self.INFINITE, False)

            if (eval > best_eval):
                best_eval = eval
                best_move = move

            board.pop()


        return best_move
    

    def alphabeta(self, board: chess.Board, depth, alpha, beta, maximising):
        inputs = board.board_fen() + "," + str(depth) + "," + str(alpha) + "," + str(beta) + "," + str(maximising)
        if inputs in self.cached:
            return float(self.cached[inputs])
        
        if depth == 0:
            return self.evaluate3(board)

        moves = list(board.legal_moves)

        if len(moves) == 0:
            return self.evaluate3(board)

        if maximising:  # maximising
            eval = float("-inf")
            for move in moves:
                board.push(move)
                eval = max(eval, self.alphabeta(board, depth-1, beta, alpha, False))  # Fix function name
                board.pop()

                if eval > beta:
                    break
                
                alpha = max(alpha, eval)

        else:   # minimising
            eval = float("inf")
            for move in moves:
                board.push(move)
                eval = min(eval, self.alphabeta(board, depth-1, beta, alpha, True))  # Fix function name
                board.pop()

                if eval < alpha:
                    break
                
                beta = min(beta, eval)
            

        self.cached[inputs] = eval
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
    
    
    def evaluate3(self, board: chess.Board):
        score = 0
        score += heuristics.material(board, 100)
        score += heuristics.piece_moves(board, 50)
        score += heuristics.pawn_structure(board, 1)
        score += heuristics.in_check(board, 1)

        return score
    
    def write_cache(self):
        # with open("cached.txt", "w") as file:
        #     for input in self.cached.keys():
        #         file.write(input + ":" + str(self.cached[input]) + "\n")
        try:
            script_directory = os.path.dirname(os.path.abspath(__file__))

            with open(os.path.join(script_directory, "cached.txt"), "w") as file:
                
                for input in self.cached.keys():
                    file.write(input + ":" + str(self.cached[input]) + "\n")

        except Exception as e:
            print(f"An error occurred: {e}")
                
        
    def order_moves(self, board, moves):
        move_scores = []

        for move in moves:
            score = 0

            if board.is_capture(move) and board.piece_at(move.to_square) is not None:
                score += 10 * self.PIECE_VALUES[board.piece_at(move.to_square).piece_type] - self.PIECE_VALUES[board.piece_at(move.from_square).piece_type]

            move_scores.append(score)

        return util.bubble_sort(moves, move_scores)
