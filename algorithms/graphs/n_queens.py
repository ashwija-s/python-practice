def dfs_n_queens(n):
    if n < 1:
        return []
    cols = set()
    negdiag = set() #r- col
    posdiag = set() #r + col

    res = []
    board = []
    def backtrack(r):
        if r == n:
            
            res.append(board[:]) 
            return

        for col in range(n):
            if col in cols or (r + col) in posdiag or (r - col) in negdiag:
                continue
            cols.add(col)
            posdiag.add(r + col)
            negdiag.add(r - col)
            board.append(col)

            backtrack(r + 1)

            cols.remove(col)
            posdiag.remove(r + col)
            negdiag.remove(r - col)
            board.pop()
    backtrack(0)
    return res