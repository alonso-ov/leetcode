class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        result = ""

        i, j = 0, 0

        # don't break out of loop until both iterators reach end
        while i < len(word1) or j < len(word2):

            # once iterator reaches end it will stop appending letters
            # since word1 conditional comes first, word1 letters will append first
            if i < len(word1):
                result += word1[i]
                i += 1
            if j < len(word2):
                result += word2[j]
                j += 1

        return result