class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """sumary_line
        
        Keyword arguments: subsequence each other
        argument -- determines whether second sequence is a subsequence or not
        Return: True if second sequence is a subsequence or False otherwise
        """
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return True if i == len(s) else False


if __name__ == '__main__':
    sol = Solution()
    if sol.isSubsequence("axc", "ahbgdc") == True:
        print("Is Subsequence")
    else:
        print("Not Subsequence")
    