/**
 * Source: LeetCode  222. Count Complete Tree Nodes
 * Author: ceezyyy
 * Date: 10-10-2019
 */


 /*
 Medium

 Given a complete binary tree, count the number of nodes.

 Note:

 Definition of a complete binary tree from Wikipedia:
 In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 Example:

 Input:
	 1
	/ \
   2   3
  / \  /
 4  5 6

 Output: 6

 */


#include<vector>
#include<queue>
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
		*int val;
		*TreeNode *left;
		*TreeNode *right;
		*TreeNode(int x) : val(x), left(NULL), right(NULL) {}
		*
	};

	int countNodes(TreeNode* root) {
		vector<int> res;
		queue<TreeNode*> q;
		if (!root)
			return 0;
		q.push(root);  // the first element
		while (!q.empty()) {
			TreeNode* node = q.front();
			q.pop();
			if (node->left)
				q.push(node->left);
			if (node->right)
				q.push(node->right);
			res.push_back(node->val);
		}
		return res.size();
	}
};


/**
 Runtime: 32 ms, faster than 75.47% of C++ online submissions for Count Complete Tree Nodes.
 Memory Usage: 30.2 MB, less than 5.55% of C++ online submissions for Count Complete Tree Nodes.
 */
