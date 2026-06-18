class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}"for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            w_len = int(s[i:j])
            start = j+1
            end = start + w_len
            word = s[start : end]
            i = end
            result.append(word)
        return result 
