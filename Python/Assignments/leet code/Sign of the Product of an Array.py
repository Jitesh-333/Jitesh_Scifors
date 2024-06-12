#There is a function signFunc(x) that returns:

#1 if x is positive.
#-1 if x is negative.
#0 if x is equal to 0.
#You are given an integer array nums. Let product be the product of all values in the array nums.

#Return signFunc(product).

#Example 1:
#Input: nums = [-1,-2,-3,-4,3,2,1]
#Output: 1
#Explanation: The product of all values in the array is 144, and signFunc(144) = 1

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # Initialize the product
        product = 1

        # Calculate the product of all values in the array
        for num in nums:
            product *= num

        # Determine the sign based on the product
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0
