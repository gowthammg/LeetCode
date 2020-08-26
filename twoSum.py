class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            if y in h:
                return [h[y],i]
            else:
                h[nums[i]] = i
        return []