class Solution:
    def isValid(self, s: str) -> bool:
        thingies = []

        for char in s:
            if char == "(":
                thingies.append("(")

            elif char == "{":
                thingies.append("{")

            elif char == "[":
                thingies.append("[")

            elif char == ")":
                if not thingies or thingies[-1] != "(":
                    return False
                thingies.pop()

            elif char == "}":
                if not thingies or thingies[-1] != "{":
                    return False
                thingies.pop()

            elif char == "]":
                if not thingies or thingies[-1] != "[":
                    return False
                thingies.pop()

        return len(thingies) == 0