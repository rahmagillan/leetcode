""" wow imagine trying...
class Solution:
	def greater_than_base26(self, r1, r2):
		for i in range(26):
			if r1[i] < r2[i]:
				return False
			if r1[i] > r2[i]:
				return True
		# must be equal
		return False
	
	def eq(self, r1, r2):
		for i in range(26):
			if r1[i] != r2[i]:
				return False
		return True

	# insert s into sorted_list
	def binaryInsertAlpha(self, sorted_list, str_orig, str_num_rep, i, j):
		while True:
			if i == j:
				if len(sorted_list) == 0:	# base case... empty list to insert into
					sorted_list.insert(i, (str_num_rep, [str_orig]))
				elif len(sorted_list) <= i:	# need to append to end of list
					sorted_list.append((str_num_rep, [str_orig]))
				elif sorted_list[i][0] == str_num_rep:
					sorted_list[i][1].append(str_orig)
				elif self.greater_than_base26(sorted_list[i][0], str_num_rep):
					sorted_list.insert(i, (str_num_rep, [str_orig]))
				else:
					sorted_list.insert(i + 1, (str_num_rep, [str_orig]))
				return

			mdpt = (j + i)//2

			if self.eq(sorted_list[mdpt][0], str_num_rep):
				sorted_list[mdpt][1].append(str_orig)
				return
			elif self.greater_than_base26(sorted_list[mdpt][0], str_num_rep):
				j = mdpt
			else:
				i = mdpt + 1
		
	def find_base26_rep(self, s):
		rep = [0 for i in range(26)]
		for c in s:
			idx = ord(c) - ord('a')
			rep[idx] += 1
		return rep

	def groupAnagrams(self, strs):
		res = []
		for s in strs:
			s_base26_rep = self.find_base26_rep(s)
			self.binaryInsertAlpha(res, s, s_base26_rep, 0, len(res))
		return list(map(lambda x : x[1], res))
"""

"""
class Solution:
	def groupAnagrams(self, strs):
		res = {}
		for s in strs:
			s_alpha = str(sorted(s))
			if not s_alpha in res:
				res[s_alpha] = [s]
			else:
				res[s_alpha].append(s)
		soln = []
		for k in res:
			soln.append(res[k])
		return soln
"""

# attempt #3
class Solution:
	def groupAnagrams(self, strs):
		res = {}
		for i, s in enumerate(strs):
			s_alpha = str(sorted(s))
			if not s_alpha in res:
				res[s_alpha] = [i]
			else:
				res[s_alpha].append(i)
		soln = []
		for k in res:
			soln.append([strs[i] for i in res[k]])
		return soln

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
