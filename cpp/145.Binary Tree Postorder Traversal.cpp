/**
 * Source: LeetCode  145. Binary Tree Postorder Traversal
 * Author: ceezyyy
 * Date: 10-04-2019
 */


 /*
 Hard

 Given a binary tree, return the postorder traversal of its nodes' values.

 Example:

 Input: [1,null,2,3]
    1
	 \
	  2
	 /
    3 

 Output: [3,2,1]

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
class Solution {
public:
	vector<int> res;
	vector<int> postorderTraversal(TreeNode* root) {
		postorderTraversal_Recursion(root);
		return res;
	}

	void postorderTraversal_Recursion(TreeNode* node) {
		if (node) {
			if (node->left)
				postorderTraversal_Recursion(node->left);
			if (node->right)
				postorderTraversal_Recursion(node->right);
			res.push_back(node->val);
		}
	}
};

/**
 * Runtime: 4 ms, faster than 58.08% of C++ online submissions for Binary Tree Postorder Traversal.
 * Memory Usage: 9.6 MB, less than 16.13% of C++ online submissions for Binary Tree Postorder Traversal.
 */

