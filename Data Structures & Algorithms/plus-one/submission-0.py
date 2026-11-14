class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for digit in digits:
            number *= 10
            number += digit
        number += 1
        ret = []
        for x in range(len(str(number))):
            ret.append(str(number)[x])
        return ret