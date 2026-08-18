class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "?" + s
        return result

    def decode(self, s: str) -> List[str]:
        result, pointer1 = [], 0

        while pointer1 < len(s):
            pointer2 = pointer1
            while s[pointer2] != "?":
                pointer2 += 1
            length_of_string = int(s[pointer1:pointer2])
            result.append(s[pointer2+1:pointer2+1+length_of_string])
            pointer1 = pointer2 + 1 + length_of_string
        return result