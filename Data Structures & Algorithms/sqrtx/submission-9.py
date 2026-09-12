class Solution:
    def mySqrt(self, x: int) -> int:

        def binSearch (low, high):
            mid = ((low + high) // 2)
            currSquare = mid*mid
            nextSquare = ( mid + 1)*(mid + 1)

            if currSquare <= x and nextSquare  > x:
                return mid

            if currSquare > x:
                return binSearch(low, mid - 1)
            else:

                 return binSearch(mid + 1, high)

        return binSearch(0, 46340)
