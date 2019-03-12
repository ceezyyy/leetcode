/*
Source: LeetCode 985. Sum of Even Numbers After Queries 
Author: ceezyyy
Date: 03-12-2019
*/


/*
Easy

Share
We have an array A of integers, and an array queries of queries.
For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index]. Then, the answer to the i-th query is the sum of the even values of A.
(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)
Return the answer to all queries. Your answer array should have answer[i] as the answer to the i-th query.

Example 1:
Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
Explanation:
At the beginning, the array is [1,2,3,4].
After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to A[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
1 <= queries.length <= 10000
-10000 <= queries[i][0] <= 10000
0 <= queries[i][1] < A.length

*/


#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

class Solution {
public:
	vector<int> sumEvenAfterQueries(vector<int>& A, vector<vector<int>>& queries) {
		vector<int> B; //Output array B
		int index, val;
		int sum;
		for (int i = 0; i < A.size(); i++) {
			index = queries[i][1];
			val = queries[i][0];
			A.at(index) += val;
			sum = 0; //zero each time
			for (int j = 0; j < A.size(); j++) {
				if (A[j] % 2 == 0) { //Determine whether it is even value
					sum += A[j];
				}
			}
			B.push_back(sum); //Adds a new element at the end of the vector 
		}
		return B;
	}
};

/*
Submission Detail:

Runtime: 3476 ms, faster than 14.62% of C++ online submissions for Sum of Even Numbers After Queries.
Memory Usage: 29.4 MB, less than 32.53% of C++ online submissions for Sum of Even Numbers After Queries.

*/

/*
Study Notes:

Be careful of the function of the vector:
std::vector::push_back

Do not write your code like this: 'B.at(j)=A.at(i)' in Line 59.
*/