#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#Note that you must do this in-place without making a copy of the array.
#Example 1:

#Input: nums = [0,1,0,3,12]
#Output: [1,3,12,0,0]


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_index = 0

        # Iterate through the array
        for current_index in range(len(nums)):
            if nums[current_index] != 0:
                # Swap non-zero element with the element at non_zero_index
                nums[current_index], nums[non_zero_index] = nums[non_zero_index], nums[current_index]
                non_zero_index += 1
        
