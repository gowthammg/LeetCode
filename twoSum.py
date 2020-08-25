class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        h = {nums[i]:i for i in range(len(nums))}
        #print(h)
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            l = h.get(y)
            if (i == l):
                continue
            if (l!=None):
                break
        return i,l
            