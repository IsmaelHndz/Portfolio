class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """sumary_line
        
        Keyword arguments: change, order
        argument -- change order in a list n times (k = 3 // [1,2,3,4,5,6,7] ->> [5, 6, 7, 1, 2, 3, 4])
        Return: return list
        """
        
        new_list = []
        k = k % len(nums)
        for i in range(k):
            new_list.append(nums.pop(len(nums)-k+i))
        new_list.extend(nums)
        nums[:] = new_list
        
        return nums, new_list
        
        


if __name__ == '__main__':
    sol = Solution()
    print(sol.rotate([1,2,3,4,5,6,7], 3))
    pass
