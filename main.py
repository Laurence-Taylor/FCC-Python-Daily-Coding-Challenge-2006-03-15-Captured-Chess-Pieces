def get_captured_value(pieces):
    # Create a list of all possible pieces of the chess
    list_chess_pieces = list('PPPPPPPPRRNNBBQK')
    # Remove the pieces in posesion to determinate tha ones lacked 
    for piece in pieces:
        list_chess_pieces.remove(piece)
    # if lacked the king, then checkmate
    if 'K' in list_chess_pieces:
        return "Checkmate"
    # init count variable
    points = 0
    # count points the adversary has
    for piece in list_chess_pieces:
        if piece == 'P': points += 1
        elif piece == 'R': points += 5
        elif piece == 'N' or piece == 'B': points += 3
        elif piece == 'Q': points += 9
    # return points
    return points

if __name__ == '__main__':
    print(get_captured_value(["P", "P", "P", "P", "P", "P", "R", "R", "N", "B", "Q", "K"]))
    print('-----')
    print(get_captured_value(["P", "P", "P", "P", "P", "R", "B", "K"]))
    print('-----')
    print(get_captured_value(["K", "P", "P", "N", "P", "P", "R", "P", "B", "P", "N", "B"]))
    print('-----')
    print(get_captured_value(["P", "Q", "N", "P", "P", "B", "K", "P", "R", "R", "P", "P", "B", "P"]))
    print('-----')
    print(get_captured_value(["P", "K"]))
    print('-----')
    print(get_captured_value(["N", "P", "P", "B", "K", "P", "Q", "N", "P", "P", "R", "R", "P", "P", "P", "B"]))
    print('-----')