import chess
import chess.polyglot

from . import tables
from . import util

# REMOVE THIS: This is doing alpha-beta pruning to make the best decision
# Alpha-beta pruning is 
class AI_AlphaBeta: # Class for calculating the best move
    INFINITE = 10000000 
    PIECE_VALUES = [0, 100, 300, 330, 500, 900, INFINITE] # Sets out numerical value to pieces.
    boards_evaluated = 0 # Keeps track of the number of games that the AI has evaluates

    def __init__(self):  # Initializes the AI
        pass #"pass" is run so there is no error if the function is empty.

    def get_move(self, board, depth): # This function decides the best move possible for a chess piece by implementing the alpha-beta search algorithm.
        best_eval = -self.INFINITE  # Minimax. Initializes the best move  to negative infinity 
        self.boards_evaluated = 0   # Rests the count of evaluated games to 0 after the game is completed

        moves = list(board.legal_moves)  # Makes a list of the possible moves in the board
        # print(moves)
        # moves = self.order_moves(board, moves) 
        best_move = None # Initializes the best_move variable

        for move in board.legal_moves:  # Applies the current move
            board.push(move) 

            eval = -self.alphabeta(board, depth-1, -self.INFINITE, self.INFINITE)

            if (eval > best_eval):  # Changes the best evaluation for a move if the current move gets a better result
                best_eval = eval    
                best_move = move

            board.pop()    #Removes the current move to explore others

        return best_move    # The best move for the chess piece is found

    def alphabeta(self, board, depth, alpha, beta): # By using alpha-beta pruning this function evaluates the numerical value of a move
        if depth == 0:   # Sets the condition about reaching to the last possible move in the tree
            self.boards_evaluated += 1   
            return self.evaluate(board)

        moves = list(board.legal_moves)    # Makes a list of all the legal possible moves to be used in this function
        moves = self.order_moves(board, moves) # Re-assigns the variable to order the moves to improve pruning effectiveness.

        if (len(moves) == 0):    # Sets the condition for the scenario in which there are no possible moves left.
            return 0

        for move in moves:
            board.push(move)    # Iterates through the possible moves, and carries out the current move
            eval = -self.alphabeta(board, depth-1, -beta, -alpha) # evaluates the current move effectiveness by using alpha-beta pruning
            board.pop()    # Removes the current move

            if (eval >= beta):    
                return beta    # Beta cutoff: prune the branch if the opponent has a better or equal move
            if (eval > alpha):
                alpha = eval    # Updates the alpha values if the current move is better

        return eval    # Returns the evaluation for a move

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
