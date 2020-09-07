class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sor = sorted(nums)
        print(sor)
        return (sor[len(sor)-k])
    