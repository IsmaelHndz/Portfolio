"""
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. 
That is, no letter appears in a single substring more than once.
Return the minimum number of substrings in such a partition.
Note that each character should belong to exactly one substring in a partition.
"""

class Solution:
    def partitionString(self, s: str) -> int:
      
        p = ""
        c = 1
        for i in s:
            if i not in p:
                p += i
            else:
                c += 1
                p = i
        return c


if __name__ == '__main__':
   s = "ssssss"
   solution = Solution()
   print(solution.partitionString(s))