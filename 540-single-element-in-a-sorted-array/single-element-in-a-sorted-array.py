class Solution(object):
    def singleNonDuplicate(self, nums):
        left = 0
        right = 1

        while right < len(nums):
            if nums[left] == nums[right]:
                left += 2
                right += 2
            else:
                return nums[left]

        return nums[left]