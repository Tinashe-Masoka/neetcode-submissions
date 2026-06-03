class Solution:
    def isPalindrome(self, s: str) -> bool:

        forward = 0
        backward = len(s) - 1

        while forward < backward :

            while not s[forward].isalnum() and forward < backward : forward += 1
            while not s[backward].isalnum() and forward < backward : backward -= 1

            if s[forward].lower() != s[backward].lower() : return False

            forward += 1
            backward -= 1

        return True