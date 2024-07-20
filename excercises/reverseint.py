class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            rev = str(x)[::-1]
        else:   
            rev = '-'+ str(-x)[::-1]
        if x > 2**31 - 1 or x < -2**31:
            return 0
        return int(rev)

solution = Solution()

print(solution.reverse(1534236469))