class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i , value in enumerate(nums):
            temp = target - value
            if temp in seen:
                return [seen[temp], i]
            seen[value]=i
