class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Edge case: If needle is empty, LeetCode conventionally expects 0
        if not needle:
            return 0
            
        # Get lengths to define our sliding window bounds
        h_len = len(haystack)
        n_len = len(needle)
        
        # Slide the window across the haystack. 
        # We stop at (h_len - n_len + 1) because any starting index 
        # beyond that won't have enough characters left to match the needle.
        for i in range(h_len - n_len + 1):
            # Check if the current slice matches the needle
            if haystack[i:i + n_len] == needle:
                return i
                
        # If we loop through without finding a match, return -1
        return -1
        