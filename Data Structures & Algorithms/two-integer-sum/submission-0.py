class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            newTarget = target - nums[i]
            if newTarget in seen:
                return [seen[newTarget], i]
            seen[nums[i]] = i

        return [0,0]
        