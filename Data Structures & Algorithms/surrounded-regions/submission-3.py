
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = []
        m = len(board)
        for x in range(len(board)):
            if board[x][0] == "O":
                q.append([x,0])
            
            if board[x][len(board[0])-1] == "O":
                q.append([x,len(board[0])-1])


        for x in range(len(board[0])):
            if board[len(board)-1][x] == "O":
                q.append([len(board)-1,x])

            if board[0][x] == "O":
                q.append([0,x])
        
        while q:
            curr = q.pop()
            curry = curr[0]
            currx = curr[1]

            if board[curry][currx] == "O":
                board[curry][currx] = "S"
            else:
                continue

            if currx + 1 < len(board[0]):
                q.append([curry, currx + 1])
            if curry + 1 < len(board):
                q.append([curry + 1, currx])
            if currx > 0:
                q.append([curry, currx - 1])
            if curry > 0:
                q.append([curry - 1, currx])
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == "O":
                    board[x][y] = "X"
                elif board[x][y] == "S":
                    board[x][y] = "O"


        