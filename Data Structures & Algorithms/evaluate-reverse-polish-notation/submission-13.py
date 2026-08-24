from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        numbs = []

        
        for char in tokens:
            if char in ("+", "-", "/", "*"):
                if char == "+":
                    numbs.append(int(numbs.pop()) + int(numbs.pop()))

                elif char == "-":
                    numbs.append(-(int(numbs.pop()) - int(numbs.pop())))

                elif char == "/":
                    pop1 = numbs.pop()
                    pop2 = numbs.pop()
                    numbs.append(int(pop2) / int(pop1))         
                else:
                    numbs.append(int(numbs.pop()) * int(numbs.pop()))
              

            else:
                numbs.append(char)


     

        return int(numbs[-1])
        
        
