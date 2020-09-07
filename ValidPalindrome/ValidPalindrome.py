class Solution:
    def isPalindrome(self, s: str) -> bool:
        rstr, lstr = "", ""
        for i in range(len(s)):
            if (s[i].isalnum()):
                rstr = s[i].lower()+rstr
                lstr = lstr+s[i].lower()
            #print(rstr, lstr)
        return True if(lstr == rstr) else False