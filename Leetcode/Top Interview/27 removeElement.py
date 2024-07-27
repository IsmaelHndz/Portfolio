class Solution:
    def __init__(self, nums: list[int], val: int) -> int:
        a = 0
        for i in range(len(nums)):
            if nums[i-a] == val:
                del nums[i-a]
                a += 1
        
        
        
        k = len(nums)

        print("Largo de la lista: ", k,"Numero quitado:", val, nums, "numeros quitados: ", a)

prueba = Solution([3,4,3,2,2,7,2,1], 2)
                  #0 1 2 3 4 5 6 7  



                