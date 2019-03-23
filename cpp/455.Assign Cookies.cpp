/*
Source: LeetCode 455. Assign Cookies
Author: ceezyyy
Date: 03-18-2019
*/


/*
Easy

Share
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. 
Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. 
If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

Note:
You may assume the greed factor is always positive.
You cannot assign more than one cookie to one child.

Example 1:
Input: [1,2,3], [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
Example 2:
Input: [1,2], [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
You have 3 cookies and their sizes are big enough to gratify all of the children,
You need to output 2.

*/


#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
	int findContentChildren(vector<int>& g, vector<int>& s) {
		int i, j;
		int count = 0; //The sum of the content children  
		sort(s.begin(), s.end(), less<int>()); //Sort g from small to large
		sort(g.begin(), g.end(), less<int>()); //Sort s from small to large
		for (i = 0, j = 0; i < s.size() && j < g.size(); i++) {
			if (s.at(i) >= g.at(j)) {
				/*
				If si >= gj,
				the child j will be content.
				*/
				count++;
				j++;
			}
		}
		return count;
	}
};


/*
Submission Detail:

Runtime: 44 ms, faster than 68.38% of C++ online submissions for Assign Cookies.
Memory Usage: 10.2 MB, less than 100.00% of C++ online submissions for Assign Cookies.

*/
