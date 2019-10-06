/**
 * Source: LeetCode  102. Binary Tree Level Order Traversal
 * Author: ceezyyy
 * Date: 10-06-2019
 */


 /*
 Medium

 Given a binary tree, return the level order traversal of its nodes' values.
 (ie, from left to right, level by level).

 For example:

 Given binary tree [3,9,20,null,null,15,7],

	3
   / \
  9  20
	/  \
   15   7

 return its level order traversal as:

 [
  [3],
  [9,20],
  [15,7]
 ]

 */


#include<vector>
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
	vector<vector<int>> levelOrder(TreeNode* root) {
		vector<vector<int>> res;
		queue<TreeNode*> q;
		if (root == NULL)
			return res;
		q.push(root);  // enter the queue
		while (!q.empty()) {
			vector<int> temp;  // subarray, each level
			int size = q.size();
			// make sure to return the level order traversal
			while (size--) {
				TreeNode* node = q.front();
				q.pop();
				if (node->left)
					q.push(node->left);
				if (node->right)
					q.push(node->right);
				temp.push_back(node->val);
			}
			res.push_back(temp);  // each level

		}
		return res;
	}
};


/**
 * Runtime: 8 ms, faster than 57.14% of C++ online submissions for Binary Tree Level Order Traversal.
 * Memory Usage: 13.7 MB, less than 98.59% of C++ online submissions for Binary Tree Level Order Traversal.
 */
