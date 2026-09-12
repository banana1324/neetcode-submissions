class Solution:
    def mySqrt(self, x: int) -> int:

        def binSearch (low, high):
            currSquare = ((low + high) // 2)*((low + high) // 2)
            currSquare1 = (((low + high) // 2) + 1)*(((low + high) // 2) + 1)
            currSquare2 = (((low + high) // 2) - 1)*(((low + high) // 2) - 1)

            if currSquare <= x and currSquare1  > x:
                return (low + high)//2
            

            if currSquare  == x:
                return ((low + high) // 2)

            if currSquare > x:
                return binSearch(low, (low + high) // 2 - 1)
            else:

                 return binSearch((low + high) // 2 + 1, high)

        return binSearch(0, 46340)
