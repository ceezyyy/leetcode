/**
 * Source: LeetCode 872. Leaf-Similar Trees
 * Author: ceezyyy
 * Date: 10-21-2019
 */


/*
 Easy

 Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.
 For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
 Two binary trees are considered leaf-similar if their leaf value sequence is the same.
 Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 Note:
 Both of the given trees will have between 1 and 100 nodes.
 
 */


#include<iostream>
#include<algorithm>
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
	struct TreeNode {
		int val;
		TreeNode *left;
		TreeNode *right;
		TreeNode(int x) : val(x), left(NULL), right(NULL) {}
	};
	vector<int> res;
	bool leafSimilar(TreeNode* root1, TreeNode* root2) {
		vector<int> res1;  // transfer parameters
		vector<int> res2;
		DFS(root1, res1);
		DFS(root2, res2);
		return res1 == res2;
	}

	void DFS(TreeNode* node, vector<int> &r) {
		if (!node)  // always the first step, an efficient way
			return;
		if ((!node->left) && (!node->right)) {  // a leaf node
			r.push_back(node->val);
		}
		DFS(node->left, r);
		DFS(node->right, r);
	}
};


/**
 * Runtime: 0 ms, faster than 100.00% of C++ online submissions for Leaf-Similar Trees.
 * Memory Usage: 14.1 MB, less than 77.78% of C++ online submissions for Leaf-Similar Trees.
 */
