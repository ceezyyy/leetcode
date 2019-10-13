/**
 * Source: LeetCode 108. Convert Sorted Array to Binary Search Tree
 * Author: ceezyyy
 * Date: 10-13-2019
 * Reference: @Grandyang  https://www.cnblogs.com/grandyang/p/4295245.html
 */


/*
 Easy

 Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
 For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

 Example:
 Given the sorted array: [-10,-3,0,5,9],
 One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

		0
	   / \
	 -3   9
	 /   /
   -10  5

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

	TreeNode* sortedArrayToBST(vector<int>& nums) {
		int size = nums.size();
		// 0 is the left boundary, initial value
		// also, size-1 is the right boundary, initial value
		return one2Two(nums, 0, size - 1);  // HERE IS "size-1"!!!

	}

	TreeNode* one2Two(vector<int> &nums, int L, int R) {
		if (L > R)  // always the first step
			return NULL;
		int mid = L + (R - L) / 2;  // an appropriate way
		TreeNode* root = new TreeNode(nums.at(mid));  // find the root of each subtree
		root->left = one2Two(nums, L, mid - 1);  // the right boundary is the only change
		root->right = one2Two(nums, mid + 1, R);  // the left boundary is the only change
		return root;
	}
};


// Study Notes:
// binary search trees(BST), sometimes called ordered or sorted binary trees
// https://en.wikipedia.org/wiki/Binary_search_tree#Order_relation


/**
 * Runtime: 20 ms, faster than 58.37% of C++ online submissions for Convert Sorted Array to Binary Search Tree.
 * Memory Usage: 21.1 MB, less than 94.59% of C++ online submissions for Convert Sorted Array to Binary Search Tree.
 */
