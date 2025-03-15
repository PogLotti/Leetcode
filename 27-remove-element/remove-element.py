class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # two pointers

        r_idx = 0  # To track the position for valid elements
        for i in range(len(nums)):
            if nums[i] != val:
                nums[r_idx] = nums[i]
                r_idx += 1

        return r_idx