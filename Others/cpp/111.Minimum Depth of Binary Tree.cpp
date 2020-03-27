/**
 * Source: LeetCode 111. Minimum Depth of Binary Tree
 * Author: ceezyyy
 * Date: 10-12-2019
 */


 /*
  Easy

  Given a binary tree, find its minimum depth.
  The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

  Note: A leaf is a node with no children.

  Example:
  Given binary tree [3,9,20,null,null,15,7],

	  3
	 / \
	9  20
	  /  \
	 15   7
  return its minimum depth = 2.

  */


#include<iostream>
#include<algorithm>
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

	// level-order
	int minDepth(TreeNode* root) {
		queue<TreeNode*> q;
		int depth = 0;  // set a initial value
		if (!root)
			return 0;
		q.push(root);
		while (!q.empty()) {
			depth++;  // level order traversal
			for (int i = q.size(); i > 0; i--) {  // each level
				TreeNode* node = q.front();
				q.pop();
				if (!node->left && !node->right)  // the first leaf node of each level
					return depth;
				if (node->left)
					q.push(node->left);
				if (node->right)
					q.push(node->right);
			}
		}
		return 0;
	}
};


/**
 * Submission Detail:
 * Runtime: 12 ms, faster than 76.35% of C++ online submissions for Minimum Depth of Binary Tree.
 * Memory Usage: 19.4 MB, less than 100.00% of C++ online submissions for Minimum Depth of Binary Tree.
 */
