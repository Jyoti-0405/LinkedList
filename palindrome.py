class Solution:
    def __init__(self):
        pass
    def isPalindrome(self, str):
       return str == str[ : :-1 ]
    

str = "jyoti"
x = Solution()
y = x.isPalindrome(str)
if(y):
    print("yes")
else:
    print("No")


