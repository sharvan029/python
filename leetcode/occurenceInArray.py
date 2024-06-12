from typing import *
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # find number of occurence of each members
        mp = dict()
        occlist = []
        for i in range(len(arr)):
            if arr[i] in mp.keys():
                mp[arr[i]] +=1
            else:
                mp[arr[i]] =1    
        # Add it to list
        list_occ = set(list(mp.values()))
        uniq_list = set(arr)
        # Check if the list has unique values
        return len(list_occ) == len(uniq_list)
arr = [1,2,2,1,1,3]
solution = Solution()
print(solution.uniqueOccurrences(arr))