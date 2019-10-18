/**
 * Source: LeetCode 429. N-ary Tree Level Order Traversal
 * Author: ceezyyy
 * Date: 10-18-2019
 */


/*
 Easy

 Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
 
 For example, given a 3-ary tree:
 link:  https://leetcode.com/problems/n-ary-tree-level-order-traversal/
 We should return its level order traversal:

 [
     [1],
     [3,2,4],
     [5,6]
 ]

 Notes:
 The depth of the tree is at most 1000.
 The total number of nodes is at most 5000.
 
 */


#include<iostream>
#include<vector>
#include<queue>
using namespace std;

// Definition for a Node.
class Node {
public:
	int val;
	vector<Node*> children;

	Node() {}

	Node(int _val, vector<Node*> _children) {
		val = _val;
		children = _children;
	}
};

class Solution {
public:
	vector<vector<int>> levelOrder(Node* root) {
		// level order
		vector<vector<int>> res;
		queue<Node*> q;
		if (!root)
			return res;
		q.push(root);
		while (!q.empty()) {
			int size = q.size();
			vector<int> temp;
			// each level
			while (size--) {
				Node* node = q.front();
				q.pop();
				temp.push_back(node->val);
				for (Node* n : node->children) {  // N-ary Tree
					q.push(n);
				}
			}
			res.push_back(temp);
		}
		return res;
	}
};


/**
 * Runtime: 148 ms, faster than 83.22% of C++ online submissions for N-ary Tree Level Order Traversal.
 * Memory Usage: 33.8 MB, less than 83.33% of C++ online submissions for N-ary Tree Level Order Traversal.
 */
