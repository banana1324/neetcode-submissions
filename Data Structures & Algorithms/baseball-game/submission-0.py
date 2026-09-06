class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []

        for x in range(len(operations)):
            if operations[x] == "+":
                score.append(score[-2] + score[-1])

            elif operations[x] == "C":
                score.remove(score[-1])

            elif operations[x] == "D":
                score.append(score[-1] * 2)
            else:
                score.append(int(operations[x]))
            print(score)

        return sum(score)