class Solution:
    def isValid(self, s: str) -> bool:
        pairs = { ']': '[', '}': '{', ')':'('}
        curr = []
        for char in s:
            if len(curr) == 0 and char in pairs:
                return False
            
            if char not in pairs:
                curr.append(char)
            elif curr[len(curr) - 1] == pairs[char]:
                curr.pop()
            else:
                return False
        return len(curr) == 0