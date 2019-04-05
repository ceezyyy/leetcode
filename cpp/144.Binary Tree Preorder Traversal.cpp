/**
 * Source: LeetCode 144. Binary Tree Preorder Traversal
 * Author: ceezyyy
 * Date: 04-02-2019
 */


/*
Medium

Share
Given a binary tree, return the preorder traversal of its nodes¡¯ values.

Example:
Input: [1,null,2,3]
   1
	\
	 2
	/
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
 
*/


#include<iostream>
#include<vector>
using namespace std;

// Definition for a binary tree node 
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };

// Recursive implementation 
class Solution {
public:
	vector<int> preorderTraversal(TreeNode* root) {
		vector<int> res;
		POT(root, res);
		return res;
	}

	void POT(TreeNode* root, vector<int> &r) {
		if (root) {
			r.push_back(root->val);
			POT(root->left, r);
			POT(root->right, r);
		}
	}
};


/**
 * Submission Detail:
 * Runtime: 4 ms, faster than 100.00% of C++ online submissions for Binary Tree Preorder Traversal.
 * Memory Usage: 9.3 MB, less than 43.05% of C++ online submissions for Binary Tree Preorder Traversal.
 */
