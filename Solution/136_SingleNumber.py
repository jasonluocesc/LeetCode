class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result^=num
        return result

print(Solution().singleNumber([0,2,2,1,1]))