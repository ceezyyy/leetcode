/**
 * Source: LeetCode  230. Kth Smallest Element in a BST
 * Author: ceezyyy
 * Date: 10-10-2019
 */


 /*
 Medium

 Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 Note:
 You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

 Example 1:

 Input: root = [3,1,4,null,2], k = 1
    3
   / \
  1   4
   \
    2
 Output: 1
 
 Example 2:

 Input: root = [5,3,6,2,4,null,null,1], k = 3
        5
       / \
      3   6
     / \
    2   4
   /
  1
 
 Output: 3

 Follow up:
 What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? 
 How would you optimize the kthSmallest routine?

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
		int val;
		TreeNode *left;
		TreeNode *right;
		TreeNode(int x) : val(x), left(NULL), right(NULL) {}
	};

	int kthSmallest(TreeNode* root, int k) {
		vector<int> res;  // store all the elements
		queue<TreeNode*> q;
		if (!root)
			return 0;
		q.push(root);  // push the first root into  queue
		while (!q.empty()) {  // the queue is not empty
			TreeNode* node = q.front();
			q.pop();
			if (node->left)
				q.push(node->left);
			if (node->right)
				q.push(node->right);
			res.push_back(node->val);
		}
		sort(res.begin(), res.end());
		return res.at(k - 1);

	}
};


/**
 * Runtime: 24 ms, faster than 50.99% of C++ online submissions for Kth Smallest Element in a BST.
 * Memory Usage: 22.3 MB, less than 6.67% of C++ online submissions for Kth Smallest Element in a BST.
 */
