WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    # outer loop
    for i in range(size):
        # inner loop
        for j in range(size):
            if j % 2 == 0:
                print(WHITE, end=" ")
            else:
                print(BLACK, end=" ")
        print(" ")


create_chessboard(size)
