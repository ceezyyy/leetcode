/**
 * Source: LeetCode  144. Binary Tree Preorder Traversal
 * Author: ceezyyy
 * Date: 10-03-2019
 */


/*
Medium

Given a binary tree, return the preorder traversal of its nodes' values.

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

// preorderTraversal_Recursion
class Solution {
public:
	vector<int> preorderTraversal(TreeNode* root) {
		vector<int> res;  // store the result
		POT_Recursion(root, res);
		return res;
	}

	void POT_Recursion(TreeNode *node, vector<int> &r) {
		if (!node)
			return;
		r.push_back(node->val);
		POT_Recursion(node->left, r);
		POT_Recursion(node->right, r);
	}
};


/**
 * Runtime: 4 ms, faster than 58.93% of C++ online submissions for Binary Tree Preorder Traversal.
 * Memory Usage: 9.4 MB, less than 44.83% of C++ online submissions for Binary Tree Preorder Traversal.
 */


// preorderTraversal_Iteration
class Solution {
public:
	vector<int> preorderTraversal(TreeNode* root) {
		vector<int> res;  // store the result
		stack<TreeNode*> s_node;
		if (root) {  // determine the root is empty or not!
			s_node.push(root);
			POT_Iteration(s_node, res);
		}
		return res;
	}

	void POT_Iteration(stack<TreeNode*> &s, vector<int> &r) {
		while (!s.empty()) {
			TreeNode *node = s.top();
			r.push_back(node->val);
			s.pop();
			if (node->right)  // determine the node is empty or not!
				s.push(node->right);
			if (node->left)
				s.push(node->left);
		}
		return;
	}
};


/**
 * Runtime: 0 ms, faster than 100.00% of C++ online submissions for Binary Tree Preorder Traversal.
 * Memory Usage: 9 MB, less than 100.00% of C++ online submissions for Binary Tree Preorder Traversal.
 */


/**
 * Study Notes:
 * Determine the node is empty or not
 * Test the situation that is NULL([])
 */