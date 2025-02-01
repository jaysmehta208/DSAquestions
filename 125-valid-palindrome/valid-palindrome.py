class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""
        # print(ord('0'))
        # print(ord('9'))
        # return True
        for i in s.lower():
            if (ord(i) >= ord('a') and ord(i) <= ord('z')) or (ord(i) >= ord('A') and ord(i) <= ord('Z')) or (ord(i) >= ord('0') and ord(i) <= ord('9')):
                r+=i
        return r == r[::-1]