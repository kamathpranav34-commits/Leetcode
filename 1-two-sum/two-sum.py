class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            required = target - nums[i]

            if required in nums[i + 1:]:
                j = nums.index(required, i + 1)
                return [i, j]