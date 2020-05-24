class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openingBrackets = ['{', '[', '(']
        closingBrackets = ['}', ']', ')']

        for ch in s:
            if ch in closingBrackets:
                matchingOpeningBracket = openingBrackets[closingBrackets.index(ch)]
                if len(stack) == 0 or (stack.pop() != matchingOpeningBracket):
                    return False
            else:
                stack.append(ch)
        return not len(stack)

t = Solution()
print(t.isValid('{[]}'))