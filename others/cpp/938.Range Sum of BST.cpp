/**
 * Source: LeetCode 938. Range Sum of BST
 * Author: ceezyyy
 * Date: 10-14-2019
 */


/*
 Easy

 Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
 The binary search tree is guaranteed to have unique values.

 Example 1:
 Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
 Output: 32

 Example 2:
 Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
 Output: 23

 Note:
 The number of nodes in the tree is at most 10000.
 The final answer is guaranteed to be less than 2^31.
 
 */


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
	int res = 0;
	int rangeSumBST(TreeNode* root, int L, int R) {
		if (!root)  // always the first step in binary tree
			return 0;
		DFS(root, L, R);
		return res;
	}

	// node->left->val < node->val < node->right->val
	void DFS(TreeNode* node, int L, int R) {
		if (!node)
			return;
		// judgment one
		if ((node->val >= L) && (node->val <= R)) 
			res += node->val;
		// judgment two
		if (L < node->val)  // the left 'remain'
			DFS(node->left, L, R);
		// judgment three
		if (node->val < R)  // the right 'remain'
			DFS(node->right, L, R);
	}
};


/**
 * Runtime: 152 ms, faster than 54.94% of C++ online submissions for Range Sum of BST.
 * Memory Usage: 41.2 MB, less than 82.73% of C++ online submissions for Range Sum of BST.
 */
