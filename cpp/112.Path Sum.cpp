/**
 * Source: LeetCode  112. Path Sum
 * Author: ceezyyy
 * Date: 10-07-2019
 */


 /*
 Easy

 Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

 Note: A leaf is a node with no children.

 Example:

 Given the below binary tree and sum = 22,

	   5
	  / \
	 4   8
	/   / \
   11  13  4
  /  \      \
 7    2      1

 return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

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
	struct TreeNode {
		int val;
		TreeNode *left;
		TreeNode *right;
		TreeNode(int x) : val(x), left(NULL), right(NULL) {}
	};

	bool hasPathSum(TreeNode* root, int sum) {
		// "exist one"
		if (!root)  
			return false;
		// "exist two"
		else {
			if (root->left == NULL && root->right == NULL && root->val == sum)  // a leaf
				return true;  
			else {
				return (hasPathSum(root->left, sum - (root->val)) || hasPathSum(root->right, sum - (root->val)));
			}
		}
	}
};


/**
 * Runtime: 16 ms, faster than 41.16% of C++ online submissions for Path Sum.
 * Memory Usage: 19.9 MB, less than 81.25% of C++ online submissions for Path Sum.
 */


 /**
  * Study Notes:
  * Binary Tree: Recursion
  */
