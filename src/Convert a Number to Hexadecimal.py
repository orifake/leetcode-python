class Solution:
    def toHex(self, num: int) -> str:
        if not num:
            return "0"
        hex, result = "0123456789abcdef", ""
        while num and len(result) < 8:
            result = hex[num & 0xf] + result
            num >>= 4
        return result