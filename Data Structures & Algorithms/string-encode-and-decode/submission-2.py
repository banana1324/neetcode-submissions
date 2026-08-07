class Solution:

    def encode(self, strs: List[str]) -> str:
        amongus = ""
        for word in strs:
            amongus = amongus + str(len(word))
            amongus = amongus + "é"
            amongus = amongus + word

        return amongus
        
    def decode(self, s: str) -> List[str]:
        sus = []
        beginind = 0
        endind = 1
        x=0
        while x < (len(s)):
            y=x
            while s[y] != "é":
                y+=1
            length = int(s[x:y])
            sus.append(s[y+1:y+1+length])
            x = y + 1 + length
        return sus