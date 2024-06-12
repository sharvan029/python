class Soluton():
    from typing import List
    def sortColors(self, nums: List[int]):
        list_red =[]
        list_blue = []
        list_white = []
        for i,x in enumerate(nums):
            if x ==0:
                list_red.append(x)
            elif x==1:
                list_white.append(x)
            else:
                list_blue.append(x)
        nums.clear()
        nums = list_red + list_white + list_blue
        print(nums)
nums = [0,0,1,2,0,1,0]
solution = Soluton()
solution.sortColors(nums)