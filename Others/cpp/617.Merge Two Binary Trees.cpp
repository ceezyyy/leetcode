/**
 * Source: LeetCode 617. Merge Two Binary Trees
 * Author: ceezyyy
 * Date: 10-21-2019
 */


/*
 Easy

 Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
 You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

 Example 1:
 Input: 
	 Tree 1                     Tree 2                  
           1                         2                             
          / \                       / \                            
         3   2                     1   3                        
        /                           \   \                      
       5                             4   7                  
 Output: 
 Merged tree:
	      3
	     / \
	    4   5
	   / \   \ 
	  5   4   7

 Note: The merging process must start from the root nodes of both trees.
 
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

	TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
		if (!t1)
			return t2;
		if (!t2)
			return t1;
		t1->val = t1->val + t2->val;
		t1->left = mergeTrees(t1->left, t2->left);
		t1->right = mergeTrees(t1->right, t2->right);
		return t1;
	}
};


/**
 * Runtime: 40 ms, faster than 60.89% of C++ online submissions for Merge Two Binary Trees.
 * Memory Usage: 13.5 MB, less than 97.22% of C++ online submissions for Merge Two Binary Trees.
 */
