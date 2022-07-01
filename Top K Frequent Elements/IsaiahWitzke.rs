use std::collections::HashMap;

struct Solution {}

impl Solution {

	/// first item in each element is the freq count
	/// second item in each element is the value
	/// inserts so that freq count is in descending order
	fn binary_insert(list: &mut Vec<(i32, i32)>, e: (i32, i32)) {
		let (mut i, mut j) = (0, list.len());
		
		if list.len() == 0 {
			list.push(e);
			return;
		}

		loop {
			if i == j {
				if list.len() <= i {	// in case need to append to end of list
					list.push(e);
				} else if list[i].0 > e.0 {
					list.insert(i + 1, e);
				} else {
					list.insert(i, e);
				}
				return;
			}

			let mdpt = (j + i)/2;

			if list[mdpt].0 > e.0 {
				i = mdpt + 1;
			} else {
				j = mdpt;
			}
		}
	}
	   


    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
		let mut freq_hm = HashMap::new();
		for num in nums.into_iter() {
			freq_hm.insert(
				num,
				if freq_hm.contains_key(&num) { freq_hm[&num] + 1 } else { 1 });
		}

		let mut freq_list: Vec<(i32, i32)> = Vec::new();
		for (key, value) in freq_hm.into_iter() {
			let e = (value, key);
			Self::binary_insert(&mut freq_list, e);
		}

		let mut sol: Vec<i32> = Vec::new();
		for i in 0..(k as usize) {
			sol.push(freq_list[i].1)
		}

		return sol;
    }
}

fn main() {
	let input = vec![1,1,1,2,2,3];
	let v2 = Solution::top_k_frequent(input, 2);
	println!("{:?}", v2);
}