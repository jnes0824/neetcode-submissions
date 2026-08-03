class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0 #目前已經進入第幾層，也就是最少跳了幾次。
        current_end = 0 #使用目前的 jumps 次數，最遠可以到達的 index。
        farthest = 0 #掃描目前這一層的所有 index 後，再跳一次最遠可以到達哪裡。

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps

"""
BFS
↓
發現每一層的位置是連續區間
↓
一層不需要保存所有 index，只記右邊界
↓
下一層也只要記最遠右邊界
↓
queue 消失
↓
得到 O(1) space 的 Greedy
"""