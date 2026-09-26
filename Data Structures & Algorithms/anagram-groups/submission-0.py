class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss not in map:
                map[ss] = [s]
            else:
                map[ss].append(s)
        return list(map.values())