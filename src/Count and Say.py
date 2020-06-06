class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def count(string):    
            V = deque()
            N = 1
            for i in range(0, len(string) - 1):
                if string[i] == string[i+1]:
                    N += 1
                else:
                    V.append(str(N))    
                    V.append(string[i])
                    N = 1   
            V.append(str(N))        
            V.append(string[-1])
            return "".join(V)
    
        if n == 1:
            return "1"
        else:
            return count(self.countAndSay(n-1))  