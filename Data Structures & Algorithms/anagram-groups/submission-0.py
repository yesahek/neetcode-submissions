class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in results:
                results[sorted_s].append(s)
            else:
                results[sorted_s] = [s]
        return list(results.values())