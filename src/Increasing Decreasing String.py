class Solution:
    def sortString(self, s: str) -> str:
        if not s:
            return ''
        
        s = list(s)
        ans = []
        while s:
            # increasing: 递增
            temp_list = list(set(s))  # set可以去重
            temp_list.sort(key=lambda c: ord(c))  # ord()：转化ASCII字符为相应的数字
            for i in temp_list:
                ans.append(i)
                s.remove(i)
            
            # decreasing: 递减
            temp_list = list(set(s))
            temp_list.sort(key=lambda c: ord(c), reverse=True)
            for i in temp_list:
                ans.append(i)
                s.remove(i)
        return ''.join(ans)

t = Solution()
print(t.sortString("aaaabbbbcccc"))