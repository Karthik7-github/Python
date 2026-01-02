class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        s={
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }
        n=len(digits)
        for i in range(0,1,1):
            if n==0:
                a=[]
            if n>=1:
                for i in digits:
                    for j in s[i]:
                        a.append(i)
                        if n>=2:
                            for i in a:
                                for j in digits[1]:
                                    a.append(i+j)
                                    if n>=3:
                                        for x in a:
                                            for y in digits[3]:
                                                a.append(i+j)
                                                if n>=4:
                                                    for z in a:
                                                        for d in digits[3]:
                                                            a.append(i+d)
                                                else:
