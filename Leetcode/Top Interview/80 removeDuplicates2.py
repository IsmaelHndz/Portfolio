class Solution:
    def removeDuplicates(nums: list[int]) -> int:
        """sumary_line
        
        Keyword arguments: no more than two same elements in the list
        argument -- delete duplicates from the list
        Return: return the large of the list without duplicates
        """
        sorted_list = set(nums)
        for element in sorted_list:
            count = nums.count(element)
            if count > 2:
                for _ in range(count - 2):
                    nums.remove(element)
        k = len(nums)
        return k