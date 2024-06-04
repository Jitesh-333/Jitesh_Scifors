#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create dictionaries to store character frequencies
        freq_s = {}
        freq_t = {}

        # Count characters in s
        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1

        # Count characters in t
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1

        # Compare character frequencies
        return freq_s == freq_t
