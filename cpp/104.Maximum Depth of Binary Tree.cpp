/**
 * Source: LeetCode  104. Maximum Depth of Binary Tree
 * Author: ceezyyy
 * Date: 10-05-2019
 */


 /*
 Medium

 Given a binary tree, find its maximum depth.
 The maximum depth is the number of nodes
 along the longest path from the root node down to the farthest leaf node.

 Note: A leaf is a node with no children.

 Example:

 Given binary tree [3,9,20,null,null,15,7],

	 3
	/ \
   9  20
	 /  \
	15   7
 return its depth = 3.

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

#include<algorithm>
using namespace std;

class Solution {
public:
	struct TreeNode {
		int val;
		TreeNode *left;
		TreeNode *right;
		TreeNode(int x) : val(x), left(NULL), right(NULL) {}
	};
	//1. return if root is null
	//2. if root is a leaf node:
	//3.      answer = max(answer, depth)       
	//4. maximum_depth(root.left, depth + 1)      
	//5. maximum_depth(root.right, depth + 1)    
	int ans = 0;
	int depth = 1;
	int maxDepth(TreeNode* root) {
		if (root == NULL)
			return 0;
		return max_d(root, depth);  // recursion
	}

	int max_d(TreeNode* node, int d) {  // d stands for depth
		if (node) {
			if ((!node->left) && (!node->right)) {  // is a leaf node
				ans = max(ans, d);
			}
			// is not a leaf node
			// find its left&right chilid
			// child: d(depth) + 1
			ans = max(max_d(node->left, d + 1), max_d(node->right, d + 1));
		}
		return ans;
	}
};


/**
 * Runtime: 8 ms, faster than 87.05% of C++ online submissions for Maximum Depth of Binary Tree.
 * Memory Usage: 19.6 MB, less than 46.15% of C++ online submissions for Maximum Depth of Binary Tree.
 */


