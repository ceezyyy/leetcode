/**
 * Source: LeetCode  129. Sum Root to Leaf Numbers
 * Author: ceezyyy
 * Date: 10-11-2019
 */


 /*
 Medium

 Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
 An example is the root-to-leaf path 1->2->3 which represents the number 123.
 Find the total sum of all root-to-leaf numbers.

 Note: A leaf is a node with no children.

 Example:
 Input: [1,2,3]
     1
    / \
   2   3
 Output: 25
 Explanation:
 The root-to-leaf path 1->2 represents the number 12.
 The root-to-leaf path 1->3 represents the number 13.
 Therefore, sum = 12 + 13 = 25.
 
 Example 2:
 Input: [4,9,0,5,1]
     4
    / \
   9   0
  / \
 5   1
 Output: 1026
 Explanation:
 The root-to-leaf path 4->9->5 represents the number 495.
 The root-to-leaf path 4->9->1 represents the number 491.
 The root-to-leaf path 4->0 represents the number 40.
 Therefore, sum = 495 + 491 + 40 = 1026.
 
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

	int sumNumbers(TreeNode* root) {
		return sumNumbersDFS(root, 0);

	}

	int sumNumbersDFS(TreeNode* node, int sum) {
		if (!node)
			return 0;
		sum = sum * 10 + node->val;  // a very useful approach
		if ((!node->left) && (!node->right)) {  // a leaf node
			return sum;
		}
		return sumNumbersDFS(node->left, sum) + sumNumbersDFS(node->right, sum);
	}
};


/**
 * Runtime: 0 ms, faster than 100.00% of C++ online submissions for Sum Root to Leaf Numbers.
 * Memory Usage: 12.4 MB, less than 92.31% of C++ online submissions for Sum Root to Leaf Numbers.
 */
