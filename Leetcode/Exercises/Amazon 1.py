"""
You are given two positive integers n and k. 
A factor of an integer n is defined as an integer i where n % i == 0.
Consider a list of all factors of n sorted in ascending order, 
return the kth factor in this list or return -1 if n has less than k factors.

n=12, k = 3
output = 3
Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
"""

class Solution:
    #Tiempo O(n)
    #Espacio O(n)
    def kthFactor(self, n: int, k: int) -> int:
        list = []
        for i in range(1, n+1):
            if n % i == 0:
                list.append(i)
                if len(list) == k: break
            else:
                continue
        return list[k-1] if k <= len(list) else -1

class Solution:
    #Tiempo O(n)
    #Espacio O(1)
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        for i in range(1, n+1):
            if n % i == 0:
                count += 1
                if count == k: return i
            else:
                continue
        return -1


if __name__ == '__main__':
    number = 12
    number_th = 3
    solution = Solution ()
    print(solution.kthFactor(number, number_th))