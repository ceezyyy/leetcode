/**
 * Source: LeetCode  103. Binary Tree Zigzag Level Order Traversal
 * Author: ceezyyy
 * Date: 10-09-2019
 */


 /*
 Medium

 Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

 For example:

 Given binary tree [3,9,20,null,null,15,7],
	 3
	/ \
   9  20
	 /  \
	15   7
 
 return its zigzag level order traversal as:

 [
   [3],
   [20,9],
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

	vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
		vector<vector<int>> res;
		queue<TreeNode*> q;
		if (!root)
			return res;
		q.push(root);
		// the similar as level order traversal
		while (!q.empty()) {
			vector<int> temp;
			int size = q.size();
			while (size--) {
				TreeNode* node = q.front();
				q.pop();
				temp.push_back(node->val);
				if (node->left)
					q.push(node->left);
				if (node->right)
					q.push(node->right);
			}
			res.push_back(temp);
		}
		for (int j = 1; j < res.size(); j = j + 2) {
			reverse(res.at(j).begin(), res.at(j).end());
		}
		return res;
	}
};


/**
 * Runtime: 4 ms, faster than 86.78% of C++ online submissions for Binary Tree Zigzag Level Order Traversal.
 * Memory Usage: 13.4 MB, less than 97.67% of C++ online submissions for Binary Tree Zigzag Level Order Traversal.
 */
