class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        # Numbers that should be present: 1 to n
        expected = set(range(1, n + 1))
        
        # Remove numbers that are present
        return list(expected - set(nums))
        