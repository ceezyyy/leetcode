/**
 * Source: LeetCode  226. Invert Binary Tree
 * Author: ceezyyy
 * Date: 10-07-2019
 */


 /*
 Easy

 Invert a binary tree.

 Example:

 Input:

      4
    /   \
   2     7
  / \   / \
 1   3 6   9
 
 Output:

      4
    /   \
   7     2
  / \   / \
 9   6 3   1

 Trivia:
 
 This problem was inspired by this original tweet by Max Howell:
 Google: 90% of our engineers use the software you wrote (Homebrew),
 but you can’t invert a binary tree on a whiteboard so f*** off.

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

	TreeNode* invertTree(TreeNode* root) {
		if (!root)
			return NULL;  // TreeNode*
		TreeNode* temp = root->left;
		root->left = root->right;
		root->right = temp;
		invertTree(root->left);
		invertTree(root->right);
		return root;  // TreeNode*
	}
};


/**
 * Runtime: 4 ms, faster than 57.89% of C++ online submissions for Invert Binary Tree.
 * Memory Usage: 9 MB, less than 100.00% of C++ online submissions for Invert Binary Tree.
 */
