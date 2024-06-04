#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack#.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # Use the find() method to search for needle in haystack
        index = haystack.find(needle)

        return index if index != -1 else -1
