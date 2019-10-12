/**
 * Source: LeetCode  257. Binary Tree Paths
 * Author: ceezyyy
 * Date: 10-12-2019
 */


 /*
 Easy

 Given a binary tree, return all root-to-leaf paths.

 Note: A leaf is a node with no children.

 Example:

 Input:

    1
  /   \
 2     3
  \
   5

 Output: ["1->2->5", "1->3"]

 Explanation: All root-to-leaf paths are: 1->2->5, 1->3

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

	vector<string> binaryTreePaths(TreeNode* root) {
		vector<string> res;
		if (!root)
			return res;
		binaryTreePathsDFS(root, "", res);  // a efficient way deal with string
		return res;
	}

	void binaryTreePathsDFS(TreeNode* node, string temp, vector<string> &r) {
		if ((!node->left) && (!node->right))
			r.push_back(temp + to_string(node->val));
		if (node->left)
			binaryTreePathsDFS(node->left, temp + to_string(node->val) + "->", r);  // 'node' is a parameter!
		if (node->right)
			binaryTreePathsDFS(node->right, temp + to_string(node->val) + "->", r);
	}
};


/**
 * Runtime: 0 ms, faster than 100.00% of C++ online submissions for Binary Tree Paths.
 * Memory Usage: 11.2 MB, less than 94.74% of C++ online submissions for Binary Tree Paths.
 */
