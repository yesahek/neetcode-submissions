class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                # checking if it's number
                if num == '.':
                    continue
                
                # checking in rows
                if num in rows[i]:
                    return False
                rows[i].add(num)

                # checking in cols
                if num in cols[j]:
                    return False
                cols[j].add(num)

                # checking squares
                squares_index = (i // 3) * 3 + (j // 3)
                if num in squares[squares_index]:
                    return False
                squares[squares_index].add(num)
        return True


        