import requests


DEFAULT_WEBSERVER = "http://127.0.0.1:5000" # Default port for localhost 


def convert_to_fen(board): # Converts to Forsyth–Edwards Notation such that the read piece is equal to the piece name in FEN, FEN Notation: https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation
    peice_conversion = {
        "BK": "k",
        "BQ": "q",
        "BB": "b",
        "BN": "n",
        "BR": "r",
        "BP": "p",
        "WK": "K",
        "WQ": "Q",
        "WB": "B",
        "WN": "N",
        "WR": "R",
        "WP": "P"
    } # Dictionary of values such that each piece on the server board 

    fen = ""
    for x in range(8): # Iterates through each row 
        count = 0
        for y in range(8): # Iterates through each column piece in the current row 
            if board[x][y] in ("..", "--", "??"): # If board has any of these values (not represented as pieces) it will add one to the count, which is added to the string in accordance to FEN notation
                count += 1
            elif count > 0:
                fen += str(count) # Once a represented piece is reached, add the number of empty spaces to the fen string
                fen += piece_conversion.get(board[x][y]) # Add the piece conversion representation to the string.
                count = 0 # Resets count to begin counting again
            else:
                fen += piece_conversion.get(board[x][y]) # If there are no empty spaces, places the next piece 
        if count > 0:
            fen += str(count)
        if x != 7:
            fen += "/"

    fen += " b KQkq - 0 1"
    return fen


def read_board_network(upstream=DEFAULT_WEBSERVER):
    resp = requests.get(upstream, timeout=0.25)
    text = resp.content.decode("latin-1").strip().split("\n")
    board = [i.split() for i in text]
    return board


def read_board(filename):
    board_matrix = []
    with open(filename, "r") as f:
        for line in f:
            line_matrix = []
            for word in line.split():
                line_matrix.append(word)
            board_matrix.append(line_matrix)

    return board_matrix


def merege_sort(moves, scores):
    return moves


def bubble_sort(moves, scores):
    for i in range(1, len(scores)):
        for j in range(0, len(scores)-1):
            if (scores[j+1] > scores[j]):
                scores[j+1], scores[j] = scores[j], scores[j+1]
                moves[j+1], moves[j] = moves[j], moves[j+1]
    return moves
