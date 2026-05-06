class Solution:
    
    def hasDuplicate(self, nums:List[int]) -> bool:
        

        if len(nums) != len(set(nums)): return True 
        else: return False

        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
        

        nums.sort()
        for i in range(1, len(nums)):
            print(i)
            if nums[i-1] == nums[i]:
                return True
        return False
        


