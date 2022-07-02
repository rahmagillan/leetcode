class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_chars = ["".join(sorted(word)) for word in strs]
        anagram_dict = {}
        for i in range(len(strs)):
            anagram_dict.setdefault(sorted_chars[i], []).append(i)
        anagrams = []
        for key in anagram_dict:
            anagrams.append([strs[index] for index in anagram_dict[key]])
        return anagrams
