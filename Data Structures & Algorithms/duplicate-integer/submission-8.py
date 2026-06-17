class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for n in nums:
            check = nums.pop()
            if check in nums:
                return True
        return False