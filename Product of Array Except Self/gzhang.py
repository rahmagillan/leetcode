class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        rnums = nums.copy()
        rnums.reverse()
        farr = [1] * l
        barr = [1] * l
        
        for i in range(l):
            farr[i] = nums[i] * farr[i-1]
            barr[i] = rnums[i] * barr[i-1]
        barr.reverse()

        res = [1] * l
        for i in range(l):
            if i == 0:
                res[i] = barr[i+1]
            elif i == l-1:
                res[i] = farr[i-1]
            else:
                res[i] = farr[i-1] * barr[i+1]
        return res
