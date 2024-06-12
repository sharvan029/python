from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        order_height = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if order_height[i] != heights[i]:
                count +=1
        return count

l = [2,4,2,2,3,1]

solution = Solution()
print(solution.heightChecker(l))