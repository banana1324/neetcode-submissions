class Solution:
    def decodeString(self, s: str) -> str:

        def findBrackEnd(string, start):
            depth = 0

            for ind in range(start, len(string)):
                if string[ind] == "[":
                    depth += 1

                elif string[ind] == "]":
                    depth -= 1

                    if depth == 0:
                        return ind

        def solveInside(string):
            res = ""
            x = 0

            while x < len(string):

                if not string[x].isdigit():
                    res += string[x]
                    x += 1

                else:
                    # Read entire number
                    num = 0

                    while x < len(string) and string[x].isdigit():
                        num = num * 10 + int(string[x])
                        x += 1

                    # x now points at [
                    bracketEnd = findBrackEnd(string, x)

                    inside = string[x + 1:bracketEnd]

                    res += num * solveInside(inside)

                    # Jump past the entire [...]
                    x = bracketEnd + 1

            return res

        return solveInside(s)