class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        """
        move through array
        if zero
            if left and right are also zero or edge
                you can plant a flower
                iterator += 2
        """

        if n == 0:
            return True

        for i in range(len(flowerbed)):

            # the way we deal with left and right edge cases is by combinding two conditions into one
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                n -= 1
                flowerbed[i] = 1

        return n <= 0