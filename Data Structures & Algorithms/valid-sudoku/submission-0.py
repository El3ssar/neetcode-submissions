from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                elem = board[row][col]
                if elem !=".":
                    if elem in rows[row]:
                        return False
                    if elem in cols[col]:
                        return False
                    if elem in blocks[(row//3) * 3 + col//3]:
                        return False
                    rows[row].add(elem)
                    cols[col].add(elem)
                    blocks[(row//3) * 3 + col//3].add(elem)
        return True