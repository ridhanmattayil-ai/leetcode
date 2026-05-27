class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        words = s.split()

        # Length should be same
        if len(pattern) != len(words):
            return False

        # Check one-to-one mapping
        return (
            len(set(pattern)) ==
            len(set(words)) ==
            len(set(zip(pattern, words)))
        )
        
        