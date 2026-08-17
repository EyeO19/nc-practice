class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charrCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a - z; need an element for each letter of the alphabet

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return [list(s) for s in res.values()]