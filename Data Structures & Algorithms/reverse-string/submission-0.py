class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        leng = len(s)
        if leng == 1:
            return
        left = 0
        right = leng-1
        while left < leng//2:
            store = s[left]
            s[left] = s[right]
            s[right] = store
            left += 1
            right -=1 