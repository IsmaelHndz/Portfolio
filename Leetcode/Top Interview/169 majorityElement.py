class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """sumary_line
        
        Keyword arguments: more coincident element
        argument -- identifies the element that is the most repeating
        Return: the int most repeating element
        """
        max_number, count = 0, 0
        for element in nums:
            if count == 0:
                max_number = element
            count += (1 if element == max_number else -1)
        return max_number

if __name__ == '__main__':
    sol = Solution()
    print(sol.majorityElement([2, 3, 2]))
    