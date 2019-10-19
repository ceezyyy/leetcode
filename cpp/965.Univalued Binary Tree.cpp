/**
 * Source: LeetCode 965. Univalued Binary Tree
 * Author: ceezyyy
 * Date: 10-19-2019
 */


/*
 Easy

 A binary tree is univalued if every node in the tree has the same value.
 Return true if and only if the given tree is univalued.

 Example 1:
       
	   1
	  / \
     1   1
    / \   \
   1   1   1

 Input: [1,1,1,1,1,null,1]
 Output: true
 
 Example 2:
        
		2
	   / \
	  2   2
     / \  
    5   2
 
 Input: [2,2,2,5,2]
 Output: false
 

 Note:

 The number of nodes in the given tree will be in the range [1, 100].
 Each node's value will be an integer in the range [0, 99].
 
 */


#include<iostream>
using namespace std;

// Definition for a binary tree node.
class Solution {
public:
	struct TreeNode {
		int val;
		TreeNode *left;
		TreeNode *right;
		TreeNode(int x) : val(x), left(NULL), right(NULL) {}
	};

	int value = 0;
	bool isUnivalTree(TreeNode* root) {
		if (!root)
			return true;
		value = root->val;
		return isUnivalTreeDFS(root->left, value) && isUnivalTreeDFS(root->right, value);
	}

	bool isUnivalTreeDFS(TreeNode* node, int v) {
		if (!node)  // exit one
			return true;
		if ((node->val) != value)  // exit two
			return false;
		return isUnivalTreeDFS(node->left, v) && isUnivalTreeDFS(node->right, v);
	}
};


/**
 * Runtime: 0 ms, faster than 100.00% of C++ online submissions for Univalued Binary Tree.
 * Memory Usage: 10.6 MB, less than 100.00% of C++ online submissions for Univalued Binary Tree. 
 */
