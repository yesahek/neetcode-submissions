class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f"{len(s)}#{s}" 
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # check if it's start from "#"
            j = i
            while s[j] != "#":
                j += 1
            word_len = int(s[i:j])
            start = j+1
            end = start + word_len
            word = s[start:end]
            result.append(word)
            i = end
        return result

