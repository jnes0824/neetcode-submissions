from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        queue = deque([(0, 0)])  # (index, jumps)
        visited = {0}

        while queue:
            index, jumps = queue.popleft()

            for next_index in range(
                index + 1,
                min(index + nums[index], n - 1) + 1
            ):
                if next_index == n - 1:
                    return jumps + 1

                if next_index not in visited:
                    visited.add(next_index)
                    queue.append((next_index, jumps + 1))

        return 0