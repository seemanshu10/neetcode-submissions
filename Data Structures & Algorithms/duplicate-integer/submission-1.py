class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numarr = len(nums)

        set_nums = set(nums)

        if numarr != len(set_nums):
            return True
        else: 
            return False