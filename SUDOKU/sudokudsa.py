from collections import defaultdict


def sudoku_solver(sudoku):
    empty = []
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxs = defaultdict(set)
    
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == '.':
                empty.append((i,j))
            else:
                rows[i].add(sudoku[i][j])
                cols[j].add(sudoku[i][j])
                boxs[(i//3,j//3)].add(sudoku[i][j])
    
    def backtrack(index):
        if index == len(empty):
            return True
      
        i,j = empty[index]
        for no in range(1,len(sudoku[0]) + 1):
            value = str(no)
            if value not in cols[j] and value not in rows[i] and value not in boxs[(i//3,j//3)]:
            
                sudoku[i][j] = value
                rows[i].add(value)
                cols[j].add(value)
                boxs[(i//3,j//3)].add(value)
                
                if backtrack(index + 1):
                    return True
                
                sudoku[i][j] = '.'
                rows[i].remove(value)
                cols[j].remove(value)
                boxs[(i//3,j//3)].remove(value)
            
        return False
    backtrack(0)
    return sudoku
if __name__ == "__main__":
    inputs = [['1', '.', '.', '.', '.', '.', '.', '7', '.'], ['.', '.', '7', '.', '.', '4', '.', '.', '.'], ['8', '5', '3', '7', '.', '9', '.', '.', '1'], ['.', '.', '.', '4', '7', '.', '1', '.', '6'], ['.', '.', '5', '.', '.', '.', '.', '4', '.'], ['7', '.', '.', '5', '6', '1', '.', '.', '.'], ['4', '.', '.', '.', '.', '6', '3', '.', '9'], ['.', '.', '.', '.', '.', '.', '7', '.', '4'], ['.', '3', '.', '.', '4', '7', '6', '.', '.']]
    print(sudoku_solver(inputs))