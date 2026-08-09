class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
#oh boy this is gon be slow

        
        for num in range(1,10):

            for y in range(0,9):#per row
                saw = 0

                for x in range(0,9):
                    if board[y][x] == str(num):
                        saw += 1
                        if saw >1:
                            return False
                if num == 0:
                    print (saw)

            for y in range(0,9):#per colm
                saw = 0

                for x in range(0,9):
                    if board[x][y] == str(num):
                        saw += 1
                        if saw >1:
                            return False
                if num == 9:
                    print (saw)

        for boxy in range(0,9,3):
            for boxx in range(0,9,3):
                for num in range(1,10):
                    saw = 0
                    for y in range(3):
                        for x in range(3):
                                if board[boxx+x][boxy+y] == str(num):
                                    saw += 1
                                    if saw >1:
                                        return False
                    if num == 9:
                        print (saw)
        return True








