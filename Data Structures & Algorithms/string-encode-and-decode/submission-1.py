class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"#{len(s)}:{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        index = 0
        while index <len(s):
            sep = s.index(":", index)
            length = int(s[index+1:sep])
            start = sep + 1
            end = start + length
            res.append(s[start:end])
            index = end
        return res 