class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        def cal_square_sum(n: int) -> int:
            square_sum = 0
            while n > 0:
                d = n % 10
                square_sum += d * d
                n = n // 10
            return square_sum

        square_sum = cal_square_sum(n) 
        while square_sum not in s:
            if square_sum == 1:
                return True 
            else:
                s.add(square_sum)
                square_sum = cal_square_sum(square_sum) 
        return False



