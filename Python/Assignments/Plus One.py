#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#Increment the large integer by one and return the resulting array of digits
#Example 1:

#Input: digits = [1,2,3]
#Output: [1,2,4]
#Explanation: The array represents the integer 123.
#Incrementing by one gives 123 + 1 = 124.
#Thus, the result should be [1,2,4].

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1  # Initialize carry to 1 (since we're adding 1)

        # Iterate through the digits from right to left
        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry
            digits[i] = total % 10  # Update the current digit
            carry = total // 10  # Calculate the carry

        # If there's still a carry after the loop, add it as a new digit
        if carry:
            digits.insert(0, carry)

        return digits
