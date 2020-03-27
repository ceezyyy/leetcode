/**
 * Source: LeetCode  101. Symmetric Tree
 * Author: ceezyyy
 * Date: 10-07-2019
 */


 /*
 Medium

 Given a binary tree, check whether it is a mirror of itself
 (ie, symmetric around its center).

 For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

	 1
	/ \
   2   2
  / \ / \
 3  4 4  3

 But the following [1,2,2,null,3,null,3] is not:

	 1
	/ \
   2   2
	\   \
	3    3

 Note:
 Bonus points if you could solve it both recursively and iteratively.

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

	bool isSymmetric(TreeNode* root) {
		if (!root)
			return true;
		return isSymmetric_Recursion(root->left, root->right);
	}

	// determine whether the (pair of)L&R node are symmetric
	bool isSymmetric_Recursion(TreeNode* L, TreeNode* R) {
		// both L&R are NULL
		if (L == NULL && R == NULL)
			return true;
		// one of them is NULL
		else if (L == NULL || R == NULL) {
			return false;
		}
		// both L&R exist
		else {
			if ((L->val) != (R->val))
				return false;
		}
		return (isSymmetric_Recursion(L->left, R->right) && (isSymmetric_Recursion(L->right, R->left)));
	}
};


/**
 * Runtime: 4 ms, faster than 84.08% of C++ online submissions for Symmetric Tree.
 * Memory Usage: 14.6 MB, less than 100.00% of C++ online submissions for Symmetric Tree.
 */


/**
 * Study Notes:
 * Test all the cases, including the example(s) and the specific situation '[]'
 */

