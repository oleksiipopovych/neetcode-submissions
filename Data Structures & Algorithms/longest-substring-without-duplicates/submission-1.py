class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        l = r = 0
        m = 0

        while(r < len(s)):
            if s[r] not in last_seen:
                last_seen[s[r]] = r
                r += 1
                m = max(m, r-l)
            else:
                while (s[r] in last_seen):
                    del last_seen[s[l]]
                    l+= 1
        
        return m


        