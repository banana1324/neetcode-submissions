class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        assStack = []
        topPos = True
        currPos = True
        for ast in asteroids:
            currSigma = True
            while assStack and assStack[-1] > 0 and ast < 0:
                if abs(assStack[-1]) < abs(ast):
                    assStack.pop() #top < ast

                elif abs(assStack[-1]) > abs(ast):
                    currSigma = False
                    break #ast < top
                else:
                    assStack.pop()
                    currSigma = False
                    break #same size
            if currSigma:
                assStack.append(ast)

        #for ast in asteroids:
    
        return assStack
                
                    