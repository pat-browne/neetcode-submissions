class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for n in nums:
            seen[n] = seen.get(n, 0)
            seen[n] = seen.get(n) + 1
            
        for k in seen.keys():
            if seen[k] > 1:
                return True
        
        return False
