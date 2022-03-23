from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)
        
        for ele in strs:
            ret[''.join(sorted(ele))].append(ele)
        return ret.values()