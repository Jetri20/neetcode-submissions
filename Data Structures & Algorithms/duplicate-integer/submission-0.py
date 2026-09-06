class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set(nums)

        return False if len(list(x)) == len(nums) else True