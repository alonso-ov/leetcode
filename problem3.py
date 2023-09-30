class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        """
        For each kid, check if giving them all the extra candies they
        will have the greatest amout of candies than the sum of all
        the kids. If so place true to
        a resulting array that ith's location is with respect to ith
        kid
        """

        # find max

        max_candies = max(candies)

        result = []

        for kid_candies in candies:
            if kid_candies + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
            
        return result