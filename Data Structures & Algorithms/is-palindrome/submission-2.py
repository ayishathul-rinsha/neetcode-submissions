import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub(r"[^a-zA-Z0-9]","",s).lower()
        l=0
        h=len(s)-1
        while l<=h:
            if s[l]==s[h]:
                l+=1
                h-=1
            else:
                return False
        return True