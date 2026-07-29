class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 0
        for i in range(n - 1, -1, -1): #range(start, stop, step)
            if digits[i] + 1 == 10:
                carry = 1
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                carry = 0
            if carry == 0:
                return digits
        if carry == 1:
            digits.insert(0, 1) #list.insert(index, value)
        return digits
