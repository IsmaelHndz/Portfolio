class Solution:
    def isPalindrome(self, s: str) -> bool:
        """sumary_line
        
        Keyword arguments: palindrome
        argument -- determines whether this is a palindrome only with alfanumeric characters
        Return: return True if this is a palindrome, False otherwise
        """
        
        s =  "".join(filter(str.isalnum, s)).lower()
        if s[::] == s[::-1]:
            return True
        else:
            return False





if __name__ == "__main__":
    sol = Solution()
    if sol.isPalindrome("A man, a plan, a canal: Panama") == True:
        print("Es palindromo")
    else:
        print("No es palindromo")
