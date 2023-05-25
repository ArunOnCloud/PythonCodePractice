class Solution:
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target): 
        cache = {};
        res =[];
        for i in range(0,len(nums)):
            tar = target-nums[i]
            #print(str(cache[tar]))
            if cache.get(tar) is not None :
               res.append(cache.get(tar))
               res.append(i)
               #print(res)
               break
            else:
               cache[nums[i]]=i
        return res
"""
if __name__ == "__main__":
    solution= Solution()
    ans = solution.twoSum([1,2,3,87,34,12],90)
    print(ans)
"""
solution = Solution()
ans = solution.twoSum([1,2,3,87,34,12],90)
print(ans)