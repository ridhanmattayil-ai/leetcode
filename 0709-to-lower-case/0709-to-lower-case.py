class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""

        for ch in s:
            if 'A' <= ch <= 'Z':
                result += chr(ord(ch) + 32)
            else:
                result += ch

        return result
        