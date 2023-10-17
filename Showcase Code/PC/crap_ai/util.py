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

#Return a 2D list representing the board game. Using "upstream" as the variable for the URL of the "DEFAULT_WEBSERVER", this function takes board game data from the web server URL
#to represent the board's rows as a set of sublists.
def read_board_network(upstream=DEFAULT_WEBSERVER):
    resp = requests.get(upstream, timeout=0.25) #Feched the data from the web server. Isn't the timeout too short? What is the purpose of the timeout in general?
    text = resp.content.decode("latin-1").strip().split("\n") #Decodes the content from "Latin-1" encoding (which represents western alphabets), removes trailing spaces and creates substrings for every newline character
    board = [i.split() for i in text] #Makes every substring into a sublist to represent the rows of the board
    return board

#Creates a matrix representation of the board as a set of lists
def read_board(filename):
    board_matrix = []
    with open(filename, "r") as f: #Opens up a file and fetches its content as it set the mode to read (r)
        for line in f:
            line_matrix = [] #Discards previous values and creates a new list for every row of the chess table
            for word in line.split():
                line_matrix.append(word) #After splitting the row into the individual blocks, they are added individually
            board_matrix.append(line_matrix) #The individual blocks (elements) are added the board matrix

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
