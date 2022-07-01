class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # poo poo solution, please improve
        
        mydict = defaultdict(int)
        
        for i in nums:
            mydict[i] += 1
        
        return sorted(mydict, key = mydict.get, reverse = True)[:k]
