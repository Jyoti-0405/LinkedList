class Solution:
    def __init__(self):None
    

    def _isPalind(num):
        temp = num
        rev = 0
        while(num>0):
            digit = num % 10
            rev = 10*rev + digit
            num = num//10
        if(temp == rev ):
            return "yes"
        else:
            return "No"
            

x = Solution
y = x._isPalind(121)
print(y)
