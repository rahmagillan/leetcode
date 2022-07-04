class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums = Counter(nums)
        nums = sorted(nums.items(), key=lambda item: (-item[1]))
        output = []
        for i in range(k):
            output.append(nums[i][0])
        return(output)