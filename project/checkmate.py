def checkmate(board :str):
    try:
        if not isinstance(board, str):
            print("Error")
            return
        rows = board.strip().split('\n')
        num_rows = len(rows)
        if num_rows == 0 or all(row == "" for row in rows):
            print("Error")
            return
        num_cols = len(rows[0])
        if any(len(row) != num_cols for row in rows):
            print("size of board is wrong")
            return
        king_pos = None
        king_count = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if rows[r][c] == 'K':
                    king_pos = (r, c)
                    king_count += 1
        if king_count > 1 :
            print("King more than 1")
            return
        elif king_count <1:
            print("There is no King")
            return
        king_row, king_col = king_pos
        for r in range(num_rows):
            for c in range(num_cols):
                piece = rows[r][c]
                if piece == 'P':
                    if king_row - r == -1 and abs(king_col - c) == 1:
                        print("Success")
                        return
                elif piece == 'B':
                    if abs(king_row - r) == abs(king_col - c):
                        step_r = 1 if king_row > r else -1
                        step_c = 1 if king_col > c else -1
                        current_r, current_c = r + step_r, c + step_c
                        while current_r != king_row and current_c != king_col:
                            if rows[current_r][current_c] != '.':
                                path_is_clear = False
                                break
                            current_r += step_r
                            current_c += step_c
                        if path_is_clear:
                            print("Success")
                            return
                elif piece == 'R':
                    if king_row == r or king_col == c:
                        path_is_clear = True
                        if king_row == r:
                            step_c = 1 if king_col > c else -1
                            for j in range(c + step_c, king_col, step_c):
                                if rows[r][j] != '.':
                                    path_is_clear = False
                                    break
                        else:
                            step_r = 1 if king_row > r else -1
                            for i in range(r + step_r, king_row, step_r):
                                if rows[i][c] != '.':
                                    path_is_clear = False
                                    break
                        if path_is_clear:
                            print("Success")
                            return
                elif piece == 'Q':
                    if abs(king_row - r) == abs(king_col - c):
                        path_is_clear = True
                        step_r = 1 if king_row > r else -1
                        step_c = 1 if king_col > c else -1
                        current_r, current_c = r + step_r, c + step_c
                        while current_r != king_row and current_c != king_col:
                            if rows[current_r][current_c] != '.':
                                path_is_clear = False
                                break
                            current_r += step_r
                            current_c += step_c
                        if path_is_clear:
                            print("Success")
                            return
                    elif king_row == r or king_col == c:
                        path_is_clear = True
                        if king_row == r:  
                            step_c = 1 if king_col > c else -1
                            for j in range(c + step_c, king_col, step_c):
                                    path_is_clear = False
                                    break
                        else:
                            step_r = 1 if king_row > r else -1
                            for i in range(r + step_r, king_row, step_r):
                                if rows[i][c] != '.':
                                    path_is_clear = False
                                    break
                        if path_is_clear:
                            print("Success")
                            return

    except Exception:
        return
    print("Fail")