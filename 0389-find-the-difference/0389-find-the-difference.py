class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Convert strings to lists for easier manipulation
        s_list = list(s)
        t_list = list(t)
        
        # Sort both lists
        s_list.sort()
        t_list.sort()
        
        # Compare each character in the sorted lists
        for i in range(len(s)):
            if s_list[i] != t_list[i]:
                # If the characters don't match, the added letter is in t
                return t_list[i]
        
        # If all characters match except the last one, the added letter is the last one in t
        return t_list[-1]