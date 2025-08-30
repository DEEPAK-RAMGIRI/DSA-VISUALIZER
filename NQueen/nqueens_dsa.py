def queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    ans = []
    
    cols = set()
    diag1 = set()
    diag2 = set()
    flag = False
    
    def backtrack(row):
        nonlocal flag
        if row == n:
            ans.append([i[:] for i in board])
            flag = True
            return
        else:
            for col in range(n):
                if col not in cols and (row - col) not in diag1 and (row + col) not in diag2:
                    board[row][col] = 'Q'
                    cols.add(col)
                    diag1.add(row - col)
                    diag2.add(row + col)
                    
                    backtrack(row + 1)
                    
                    board[row][col] = '.'
                    cols.remove(col)
                    diag1.remove(row - col)
                    diag2.remove(row + col)
        
    backtrack(0)
    return ans[0] if flag else flag 
        
