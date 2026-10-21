def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    rs = [set() for _ in range(9)]
    cs = [set() for _ in range(9)]
    bs = [set() for _ in range(9)]

    for r, x in enumerate(board):
        for c, v in enumerate(x):
            if v == ".":
                continue
            b = (r // 3) * 3 + (c // 3)
            if v in rs[r] or v in cs[c] or v in bs[b]:
                return False
            rs[r].add(v)
            cs[c].add(v)
            bs[b].add(v)
    return True
              
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
              
print(isValidSudoku(board))
