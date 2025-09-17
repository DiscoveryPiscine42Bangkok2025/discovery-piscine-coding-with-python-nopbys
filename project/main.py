from checkmate import checkmate
def main():
    board1 = """\
R...
.K..
..P.
....\
"""
    print("Board 1 : " ,end=" ")
    checkmate(board1)
    board2 = """\
..
.K\
"""
    print("Board 2 : " ,end=" ")
    checkmate(board2)
    board3 = """\
...
.K.
..P\
"""
    print("Board 3 : " ,end=" ")
    checkmate(board3)
    board4 = """\
.R.
.K.
...\
"""
    print("Board 4 : " ,end=" ")
    checkmate(board4)
    board5 = """\
...
.K.
.R.\
"""
    print("Board 5 : " ,end=" ")
    checkmate(board5)
    board6 = """\
...
.K.
...\
"""
    print("Board 6 : " ,end=" ")
    checkmate(board6)
    board7=None
    print("Board 7 : " ,end=" ")
    checkmate(board7)
    board8 = """\
.....
.....
..K..
.....
..Q..\
"""
    print("Board 8 : " ,end=" ")
    checkmate(board8)
if __name__ == "__main__":
    main()

