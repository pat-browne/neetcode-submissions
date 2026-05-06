class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t): return True
        return False
        
        
        final_map = {}
        for i in s:
            final_map = final_map.get(i,0) +1
        for i in t:
            final_map.append(i)
        
        
        
        
        
        s_list = []
        t_list = []
        for i in s:
            s_list.append(i)
        for i in t:
            t_list.append(i)
        s_list.sort()
        t_list.sort()
        if s_list == t_list: return True
        return False
        