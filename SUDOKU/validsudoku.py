from collections import defaultdict


def valid_sudoku(sudoku):
    if len(sudoku) != len(sudoku[0]): return False
    
    rows = defaultdict(list)
    cols = defaultdict(list)
    boxs = defaultdict(list)
    
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == '.':
                continue
            elif sudoku[i][j].isdigit() and sudoku[i][j] not in cols[j] and sudoku[i][j] not in rows[i] and sudoku[i][j] not in boxs[(i//3 , j//3)]:
                cols[j].append(sudoku[i][j])
                rows[i].append(sudoku[i][j])
                boxs[(i//3 , j // 3)].append(sudoku[i][j]) 
            else: return False     
    return True
