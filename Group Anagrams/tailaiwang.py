#Group Anagrams
#https://leetcode.com/problems/group-anagrams/
#Medium, 05/02/2022
#Tailai Wang

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)
        for word in strs:
            anagrams[frozenset(Counter(word).items())].append(word)
        return anagrams.values()
				
