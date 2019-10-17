/**
 * Source: LeetCode 783. Minimum Distance Between BST Nodes
 * Author: ceezyyy
 * Date: 10-17-2019
 */


/*
 Easy

 Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

 Example :
 Input: root = [4,2,6,1,3,null,null]
 Output: 1
 
 Explanation:
 Note that root is a TreeNode object, not an array.
 The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

		  4
		/   \
	  2      6
	 / \
	1   3

 while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.

 Note:
 The size of the BST will be between 2 and 100.
 The BST is always valid, each node's value is an integer, and each node's value is different.
 
 */


#include<iostream>
#include<vector>
#include<queue>
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

	int minDiffInBST(TreeNode* root) {
		vector<int> res;
		queue<TreeNode*> q;
		int size = 0;
		if (!root)
			return 0;
		q.push(root);
		while (!q.empty()) {
			size = q.size();
			while (size--) {  // level order
				TreeNode* temp = q.front();
				q.pop();
				res.push_back(temp->val);
				if (temp->left)
					q.push(temp->left);
				if (temp->right)
					q.push(temp->right);
			}
		}
		sort(res.begin(), res.end());
		int ans = res.at(1) - res.at(0);  // initial value
		for (int i = 2; i < res.size(); i++) {
			// the minimum difference between the values of any two different nodes 
			ans = min((res.at(i) - res.at(i - 1)), ans);
		}
		return ans;
	}
};


/**
 * Runtime: 4 ms, faster than 70.88% of C++ online submissions for Minimum Distance Between BST Nodes.
 * Memory Usage: 11 MB, less than 100.00% of C++ online submissions for Minimum Distance Between BST Nodes.
 */
