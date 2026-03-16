def get_captured_value(pieces):
    set_chess_pieces = set('PPPPPPPPRRKKBBQK')
    actual_pieces = set(pieces)
    accent_pieces = set_chess_pieces - actual_pieces
    print(accent_pieces)
    return pieces

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
    print(get_captured_value(["N", "P", "P", "B", "P", "R", "Q", "P", "P", "P", "B"]))