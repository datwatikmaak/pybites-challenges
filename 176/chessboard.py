WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    r = range(size)
    rows = [' '.join(['01'[(i + p) % 2] for i in r]) for p in (WHITE, BLACK)]
    return [rows[i % 2] for i in r]


create_chessboard(8)
