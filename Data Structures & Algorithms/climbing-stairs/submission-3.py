# 「第一步」到底走 1 (剩下n - 1)還是走 2(剩下n - 2)？base case是剩下0步，剩下步數< 0代表超過了
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n+1)
        def climb(i):
            if i == 0:
                return 1
            if i < 0:
                return 0
            if cache[i] != -1:
                steps = cache[i]
            else:
                steps = climb(i-1) + climb(i-2)
                cache[i] = steps
            return steps
        return climb(n)