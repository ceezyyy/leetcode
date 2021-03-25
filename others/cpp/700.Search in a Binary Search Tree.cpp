/**
 * Source: LeetCode 700. Search in a Binary Search Tree
 * Author: ceezyyy
 * Date: 10-18-2019
 */


/*
 Easy

 Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

 For example, 
 Given the tree:
       
	     4
        / \
       2   7
      / \
     1   3

 And the value to search: 2
 You should return this subtree:

       2     
      / \   
     1   3

 In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.
 Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.
 
 */


#include<iostream>
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

	TreeNode* searchBST(TreeNode* root, int val) {
		if (!root)
			return NULL;
		return searchBSTRecursion(root, val);
	}
	TreeNode* searchBSTRecursion(TreeNode* node, int val) {
		// exit one
		if (!node)
			return NULL;
		// exit two
		if (val == (node->val))
			return node;  // return its subtree
		if (val < (node->val))
			return searchBSTRecursion(node->left, val);  // TreeNode*
		if (val > (node->val))
			return searchBSTRecursion(node->right, val);  // TreeNode*
		return NULL;  // not found
	}
};


/**
 * Runtime: 52 ms, faster than 68.10% of C++ online submissions for Search in a Binary Search Tree.
 * Memory Usage: 28.9 MB, less than 97.56% of C++ online submissions for Search in a Binary Search Tree.
 */
