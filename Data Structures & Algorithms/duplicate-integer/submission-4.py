class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDup = set(nums)
        for num in noDup:
            nums.remove(num)
        if nums:
            return True
        else:
            return False     