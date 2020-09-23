class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


t = Solution()
print(t.defangIPaddr("255.100.50.0"))