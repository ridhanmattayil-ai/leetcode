class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Remove extra spaces from start and end
        s = s.strip()
        
        # Split words and get last word length
        return len(s.split()[-1])