class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT = -(2**31)      # -2147483648
        MAX_INT = 2**31 - 1     #  2147483647 
        negative = False
        result = 0

        if x == MIN_INT:
            return 0
        
        while x != 0:
            if x > 0:
                digit = x % 10
                x = x // 10
            else:
                digit = -((-x) % 10) #若-123 % 10 == 7, 應該要得到-3
                x = -((-x) // 10) # Python 的 // 是 floor division，不是朝 0 截斷。-123 // 10會得到-13
            #這樣才能一率用result = result * 10 + digit
            if result > (MAX_INT - digit) // 10: #若result * 10 + digit後 > MAX_INT
                return 0
                
            MIN_PREFIX = -214748364
            if result < MIN_PREFIX:
                return 0

            if result == MIN_PREFIX and digit < -8:
                return 0
            result = result * 10 + digit
        
        return result

