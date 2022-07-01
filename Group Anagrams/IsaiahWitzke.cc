#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <map>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
		map<string, vector<const string *>> map_of_anagrams;
		vector<vector<string>> soln;

		for(size_t i = 0; i < strs.size(); i++) {
			string sSorted = strs[i];
			sort(sSorted.begin(), sSorted.end());
			if(map_of_anagrams.count(sSorted) == 0) {
				map_of_anagrams.insert(pair<string, vector<const string *>>(
					sSorted,
					vector<const string *>{&(strs[i])}
				));
			} else {
				map_of_anagrams.at(sSorted).push_back(&(strs[i]));
			}
		}

		for(auto x : map_of_anagrams) 	{
			soln.push_back({});
			for(auto y : x.second) {
				soln.back().push_back(*y);
			}
		}
		return soln;
    }
};

int main() {
	Solution s;
	vector<string> in {"eat","tea","tan","ate","nat","bat"};
	auto a = s.groupAnagrams(in);
	for (auto x : a) {
		for(auto y : x) {
			cout << y << ", ";
		}
		cout << endl;
	}
}