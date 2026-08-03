from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        queue = deque([(0, 0)])  # (index, jumps)
        farthest = 0 #紀錄已加入queue最遠index

        while queue:
            index, jumps = queue.popleft()
            reachable_end = min(index + nums[index], n - 1)

            for next_index in range(
                farthest + 1,
                reachable_end + 1
            ):
                if next_index == n - 1:
                    return jumps + 1

                queue.append((next_index, jumps + 1))
            
            farthest = max(farthest, reachable_end)

        return 0