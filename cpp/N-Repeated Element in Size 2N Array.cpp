/*
Source: LeetCode 961. N-Repeated Element in Size 2N Array 
Author: ceezyyy
Date: 03-05-2019
*/


/*
Easy

Share
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5

Note:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even

*/


#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
	int repeatedNTimes(vector<int>& A) {
		int len = A.size() / 2; //2N-array, N-repeated
		int count = 1;
		int ans;
		for (int i = 0; i < A.size(); i++) {
			for (int j = i + 1; j < A.size(); j++) {
				if (A.at(i) == A.at(j)) {
					count++;
					ans = A.at(i);
				}
			}
			// exactly one of these elements is repeated N times.
			if (count > 1) {  
				cout << ans;
				break;
			}
		}
		return ans;
	}
};
