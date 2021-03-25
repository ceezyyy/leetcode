/**
 * Source: LeetCode  199. Binary Tree Right Side View
 * Author: ceezyyy
 * Date: 10-09-2019
 */


 /*
 Medium

 Given a binary tree, imagine yourself standing on the right side of it, 
 return the values of the nodes you can see ordered from top to bottom.

 Example:

 Input: [1,2,3,null,5,null,4]
 Output: [1, 3, 4]

 Explanation:

	1            <---
  /   \
 2     3         <---
  \     \
   5     4       <---

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
	struct TreeNode {
		int val;
		TreeNode *left;
		TreeNode *right;
		TreeNode(int x) : val(x), left(NULL), right(NULL) {}
	};

	vector<int> rightSideView(TreeNode* root) {
		vector<int> res;
		queue<TreeNode*> q;
		if (!root)
			return res;
		q.push(root);  // the first element
		while (!q.empty()) {
			vector<int> temp_vec;  // the similar with level order traversal
			int temp_size = q.size();  // the size of each level
			for (int i = 0; i < temp_size; i++) {
				TreeNode* node = q.front();
				q.pop();
				temp_vec.push_back(node->val);
				if (node->left)  // left child
					q.push(node->left);
				if (node->right)  // right child
					q.push(node->right);
			}
			res.push_back(temp_vec.back());  // the last element is the right side node
		}
		return res;
	}
};


/**
 * Runtime: 4 ms, faster than 72.00% of C++ online submissions for Binary Tree Right Side View.
 * Memory Usage: 9.7 MB, less than 75.68% of C++ online submissions for Binary Tree Right Side View.
 */
