/**
 * Source: LeetCode 976. Largest Perimeter Triangle
 * Author: ceezyyy
 * Date: 04-12-2019
 */


#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

class Solution {
public:
	int largestPerimeter(vector<int>& A) {
		// 3 <= A.length <= 10000
		int res;
		if (A.size() == 3) {
			sort(A.begin(), A.end(), greater<int>());
			if (A.at(1) + A.at(2) > A.at(0)) {
				// the sum of any two sides is greater than the third side
				return A.at(0) + A.at(1) + A.at(2);
			}
		}
		else { // the number of sides is greater than 3
			sort(A.begin(), A.end(), greater<int>());
			for (int i = 0; (i + 2) < A.size(); i++) {
				if (A.at(i + 1) + A.at(i + 2) > A.at(i)) {
					return A.at(i) + A.at(i + 1) + A.at(i + 2);
				}
			}
		}
		return 0; // just judge the situation that matches the problem, and the rest will return 0
	}
};


/**
 * Submission Detail:
 * Runtime: 56 ms, faster than 71.90% of C++ online submissions for Largest Perimeter Triangle.
 * Memory Usage: 10.4 MB, less than 100.00% of C++ online submissions for Largest Perimeter Triangle.
 */