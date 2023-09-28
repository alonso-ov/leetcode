class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        """
        make sure lenght of x is a factor of the entire length of the
        shorest string, otherwise it will be impossible to create
        that string from x

        string1/string2 % length(x) == 0
        """

        # get both lengths
        len1, len2 = len(str1), len(str2)

        def isDivisor(r):
            # check if r is a factor of both lengths
            # if either returns anthing but zero then it is not
            # a factor for both str1 and str2
            if len1 % r or len2 % r:
                return False

            #calculate factors
            fact1, fact2 = len1 // r, len2 // r
            
            return str1[:r] * fact1 == str1 and str1[:r] * fact2 == str2


        # iterate backwards, which guaratees first match is longest
        # prefix
        # right for right index
        # pick the smallest length because prefix can only be up to
        # smallest string
        for r in range(min(len1, len2), 0, -1):

            # if prefix is a divisor of both str1 and str2 then return
            # prefix
            if isDivisor(r):
                # we can just say str1 because prefix will be the same
                # in both strings
                return str1[:r]

        # if no prefix is found then return empty string
        return ""
    
Solution().gcdOfStrings("LEET", "CODE")