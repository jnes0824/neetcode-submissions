class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #nlogn
        result = []
        s = set()
        for i, num in enumerate(nums):
            target = 0 - num
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    if (num, nums[l], nums[r]) not in s:
                        result.append([num, nums[l], nums[r]])
                        s.add((num, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
        
        return result

