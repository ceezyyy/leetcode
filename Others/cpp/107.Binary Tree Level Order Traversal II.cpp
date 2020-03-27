/**
 * Source: LeetCode 107. Binary Tree Level Order Traversal II
 * Author: ceezyyy
 * Date: 10-20-2019
 */


/*
 Easy

 Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

 For example:
 Given binary tree [3,9,20,null,null,15,7],
 	 3
    / \
   9  20
	 /  \
    15   7
 
 return its bottom-up level order traversal as:
 [
   [15,7],
   [9,20],
   [3]
 ]
 
 */


#include<iostream>
#include<algorithm>
#include<queue>
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

	vector<vector<int>> levelOrderBottom(TreeNode* root) {
		vector<vector<int>> res;
		queue<TreeNode*> q;
		if (!root)
			return res;
		q.push(root);
		while (!q.empty()) {
			int size = q.size();
			vector<int> temp;
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
		reverse(res.begin(), res.end());
		return res;
	}
};


/**
 * Runtime: 4 ms, faster than 95.28% of C++ online submissions for Binary Tree Level Order Traversal II.
 * Memory Usage: 13.8 MB, less than 97.30% of C++ online submissions for Binary Tree Level Order Traversal II.
 */
