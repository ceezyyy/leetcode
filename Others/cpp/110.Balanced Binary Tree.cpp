/**
 * Source: LeetCode 110. Balanced Binary Tree 
 * Author: ceezyyy
 * Date: 10-12-2019
 * Reference: @Grandyang  https://www.cnblogs.com/grandyang/p/4045660.html
 */


/*
 Easy

 Given a binary tree, determine if it is height-balanced.
 For this problem, a height-balanced binary tree is defined as:
 a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

 Example 1:
 Given the following tree [3,9,20,null,null,15,7]:

	 3
    / \
   9  20
	 /  \
    15   7
 
 Return true.

 Example 2:
 Given the following tree [1,2,2,3,3,null,null,4,4]:

	    1
	   / \
	  2   2
	 / \
    3   3
   / \
 4   4

 Return false.
 
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
	// a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
	// pay attention to every node
	bool isBalanced(TreeNode* root) {
		// recursion
		if (!root)  // exit one
			return true;
		if (abs(getDepth(root->left) - getDepth(root->right)) > 1)  // exit two
			return false;
		return (isBalanced(root->left)) && (isBalanced(root->right));  // formula
	}

	int getDepth(TreeNode* node) {
		if (!node)  // exit
			return 0;
		return 1 + max(getDepth(node->left), getDepth(node->right));  // the next level: plus one
	}
};


/**
 * Submission Detail:
 * Runtime: 12 ms, faster than 84.50% of C++ online submissions for Balanced Binary Tree.
 * Memory Usage: 17.2 MB, less than 93.22% of C++ online submissions for Balanced Binary Tree.
 */
