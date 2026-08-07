class Solution:

    def encode(self, strs: List[str]) -> str:
        amongus = ""
        for word in strs:
            amongus = amongus + word
            amongus = amongus + "é"
        return amongus
        
    def decode(self, s: str) -> List[str]:
        sus = []
        beginind = 0
        endind = 1
        for letter in s:
            if letter == 'é':
                sus.append(s[beginind:endind-1])
                beginind = endind 
            endind += 1
        return sus