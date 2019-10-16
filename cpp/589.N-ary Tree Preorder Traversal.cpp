/**
 * Source: LeetCode 589. N-ary Tree Preorder Traversal
 * Author: ceezyyy
 * Date: 10-16-2019
 */


/*
Given an n - ary tree, return the preorder traversal of its nodes' values.

For example, given a 3 - ary tree :

       1
     / / \
	3 2   4
   / \
  5   6

Return its preorder traversal as : [1, 3, 5, 6, 2, 4].

 */


#include<iostream>
#include<vector>
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
	vector<int> res;
	vector<int> preorder(Node* root) {
		if (!root)  // alway the first step in 'tree'
			return res;
		DFS(root);
		return res;  // do not forget to return value
	}

	void DFS(Node* node) {
		if (!node)
			return;
		res.push_back(node->val);
		for (Node* temp : node->children) {  // each children
			DFS(temp);  // recursion
		}
	}
};


/**
 * Runtime: 156 ms, faster than 44.49% of C++ online submissions for N-ary Tree Preorder Traversal.
 * Memory Usage: 32.5 MB, less than 94.74% of C++ online submissions for N-ary Tree Preorder Traversal.
 */
