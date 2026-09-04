class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for words in strs:
            key=tuple(sorted(words))
            if key in group:
                group[key].append(words)
            else:
                group[key]=[words]
        return list(group.values())