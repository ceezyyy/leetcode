/**
 * Source: LeetCode 637. Average of Levels in Binary Tree
 * Author: ceezyyy
 * Date: 10-21-2019
 */


/*
 Easy

 Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
 
 Example 1:
 Input:
     3
    / \
   9  20
     /  \
    15   7
 Output: [3, 14.5, 11]
 
 Explanation:
 The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
 
 Note:
 The range of node's value is in the range of 32-bit signed integer.
 
 */


#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
	struct TreeNode {
		int val;
		TreeNode *left;
		TreeNode *right;
		TreeNode(int x) : val(x), left(NULL), right(NULL) {}
	};

	vector<double> averageOfLevels(TreeNode* root) {
		// level order
		vector<double> res;
		queue<TreeNode*> q;
		if (!root)
			return res;
		q.push(root);
		while (!q.empty()) {
			double sum = 0;  // 'double'  
			int size = q.size();  // the size of each level
			int temp = size;  // a temporary variable
			while (size--) {
				TreeNode* node = q.front();
				q.pop();
				sum += node->val;
				if (node->left)
					q.push(node->left);
				if (node->right)
					q.push(node->right);
			}
			res.push_back(sum / temp);
		}
		return res;
	}
};


/**
 * Runtime: 20 ms, faster than 70.32% of C++ online submissions for Average of Levels in Binary Tree.
 * Memory Usage: 21.6 MB, less than 100.00% of C++ online submissions for Average of Levels in Binary Tree.
 */
