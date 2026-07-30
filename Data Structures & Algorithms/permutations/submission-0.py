class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        used = set()

        def backtrack(num):
            # 已經選了 n 個數字，得到一個 permutation
            if len(num) == n:
                ans.append(num.copy())
                return

            # 每一層都嘗試選擇所有尚未使用的數字
            for i in range(n):
                if i not in used:
                    used.add(i)
                    num.append(nums[i])

                    backtrack(num)

                    # backtracking：撤銷剛才的選擇
                    num.pop()
                    used.remove(i)

        backtrack([])
        return ans