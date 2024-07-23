from collections import deque

class MovingTotal:
    def __init__(self):
        self.data = deque()
        self.totals = {}


    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        for num in numbers:
            if len(self.data) == 3:
                total = sum(self.data)
                self.totals[total] = True
                self.data.popleft()
            self.data.append(num)

            if len(self.data) == 3:
                total = sum(self.data)
                self.totals[total] = True

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        return total in self.totals
    
if __name__ == "__main__":
    movingtotal = MovingTotal()
    
    movingtotal.append([1, 2, 3, 4])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))
    
    movingtotal.append([5])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))