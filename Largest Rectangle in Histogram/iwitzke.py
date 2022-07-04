# TODO: make it faster... this is accepted but is worse than 95% of solutions
from typing import *

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

		# base cases
        if len(heights) == 1:
            return heights[0]
        if len(heights) == 0:
            return 0

		# divide
        mid = len(heights) // 2
        l = self.largestRectangleArea(heights[:mid])
        r = self.largestRectangleArea(heights[mid:])

		# conquer
        i = mid - 1
        j = mid
        min_height = min(heights[i],heights[j])
        max_spanning_area = 0

        while j - i + 1 <= len(heights):
            min_height = min(min_height, heights[i], heights[j])
            temp_area = (j - i + 1) * min_height
            max_spanning_area = max(max_spanning_area, temp_area)
            if i == 0:
                j+=1
            elif j == len(heights) - 1:
                i-=1
            elif heights[j+1] >= heights[i-1]:
                j+=1
            else:
                i-=1
        
        return max(l, r, max_spanning_area)



s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))

