class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers in nums that add up to target.
        Returns the indices of the two numbers.
        """
        d = {}

        for i in range(len(nums)):
            c = target - nums[i]

            if c in d:
                return [d[c], i]

            d[nums[i]] = i