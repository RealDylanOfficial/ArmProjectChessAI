import random
import time

import chess

from crap_ai.ai import AI_AlphaBeta
from crap_ai.util import read_board_network, convert_to_fen
import sys

##############
# set to true if you're debugging and not running it via the console
debugging = False
# use to set agent and depth without console while debugging
agent_type = "random"
depth = 4
##############

if len(sys.argv) < 3 and debugging == False:
  print("Usage: python ai_test.py <agent_type> <search_depth>")
  print("Agent types: random, human")
  sys.exit(1)
elif debugging == False:
  agent_type = sys.argv[1].lower()
  depth = int(sys.argv[2].lower())

if agent_type not in ["random", "human", "console"]:
    print("Invalid agent type. Please choose 'random' or 'human'.")
    sys.exit(1)



board = [["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
    ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
    ["..", "..", "..", "..", "..", "..", "..", ".."],
    ["..", "..", "..", "..", "..", "..", "..", ".."],
    ["..", "..", "..", "..", "..", "..", "..", ".."],
    ["..", "..", "..", "..", "..", "..", "..", ".."],
    ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
    ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]]

alphabeta_ai = AI_AlphaBeta()

#alphabeta_ai = ai.AI_AlphaBeta()

board = chess.Board(convert_to_fen(board))
print(board)

while True:
  if agent_type == "" or agent_type == "console" or agent_type == "human":
    # console input
    while True:
      move = input("enter move: ")
      try:
        move = chess.Move.from_uci(move)
      except:
        print("invalid move format. Must be in UCI e.g. e7e6")
        continue
      if board.is_legal(move):
        break
      else:
        print("illegal move")
        continue
  elif agent_type == "random":
    moves = []
    for x in board.legal_moves:
     moves.append(x)
    move = random.choice(moves)
    print(move)


  # webserver input
  # board = chess.Board(convert_to_fen(read_board_network()))
  
  board.push(move)
  print(board)

  # ai move

  start_time = time.time()
  ai_move = alphabeta_ai.get_move(board, depth)
  print("--- %s seconds ---" % (time.time() - start_time))
  print(ai_move)
  board.push(ai_move)
  print(board)
  print("================================")

  # time.sleep(1)