from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # idea for solution: 
        #   Get freq of letters for each word and store them 
        #   in their respective position in a 26-tuple and use this as key
        #   in ans dictionary
        
        # initialize ans dictionary
        d = defaultdict(list)
        
        # iterate over strs
        for string in strs:
            freq = [0 for _ in range(26)]
            # count the freq of letters and store word in dict
            for c in string:
                freq[ord(c)-ord('a')] += 1
            d[tuple(freq)].append(string)
            
        return list(d.values())
