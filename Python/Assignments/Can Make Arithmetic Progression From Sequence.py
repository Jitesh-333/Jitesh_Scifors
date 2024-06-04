#A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

#Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # Sort the array in ascending order
        arr.sort()

        # Calculate the common difference
        common_diff = arr[1] - arr[0]

        # Check if the remaining elements have the same difference
        for i in range(1, len(arr) - 1):
            if arr[i + 1] - arr[i] != common_diff:
                return False

        return True
