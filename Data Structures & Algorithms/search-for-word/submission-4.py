class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def match(board, word, i, j, n):
            if word[n] == board[i][j]:
                c = board[i][j]
                board[i][j] = '@'
                if n == len(word) - 1:
                    return True
            
                if j - 1 >= 0:
                    if match(board, word, i, j - 1, n + 1):
                        return True
                if i + 1 <= len(board) - 1:
                    if match(board, word, i + 1, j, n + 1):
                        return True
                if j + 1 <= len(board[0]) - 1:
                    if match(board, word, i, j + 1, n + 1):
                        return True
                if i - 1 >= 0:
                    if match(board, word, i - 1, j, n + 1):
                        return True
                board[i][j] = c
                return False
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if match(board, word, i, j, 0):
                        return True
        return False
                    

