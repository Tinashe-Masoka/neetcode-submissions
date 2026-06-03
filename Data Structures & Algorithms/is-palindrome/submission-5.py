class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_s = "".join( char.lower() for char in s if char.isalnum() )
        forward = 0
        backward = len(clean_s) - 1

        while forward < (len(clean_s)//2) :

            if clean_s[forward] != clean_s[backward] :
                return False
            forward += 1
            backward -= 1

        return True