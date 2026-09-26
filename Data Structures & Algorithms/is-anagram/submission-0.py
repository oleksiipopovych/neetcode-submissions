class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for char in s:
            chars[char] = chars.get(char, 0) + 1

        for c in t:
            if c not in chars:
                return False;
            chars[c] -= 1;
            if chars[c] == 0:
                chars.pop(c)

        return len(chars) == 0
        