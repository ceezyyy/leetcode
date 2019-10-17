/**
 * Source: LeetCode 559. Maximum Depth of N-ary Tree
 * Author: ceezyyy
 * Date: 10-17-2019
 */


/*
 Easy

 Given a n-ary tree, find its maximum depth.
 The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
 For example, given a 3-ary tree:

 link:  https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
 
 We should return its max depth, which is 3.

 Note:
 The depth of the tree is at most 1000.
 The total number of nodes is at most 5000.

 */


#include<iostream>
#include<algorithm>
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
	int ans = 0;
	int maxDepth(Node* root) {
		if (!root)
			return 0;
		maxDepthDFS(root, 1);
		return ans;
	}

	void maxDepthDFS(Node* node, int d) {  // d stands for depth
		if (!node)
			return;
		ans = max(d, ans);
		for (Node* temp : node->children) {
			maxDepthDFS(temp, d + 1);
		}
	}
};


/**
 * Runtime: 144 ms, faster than 61.94% of C++ online submissions for Maximum Depth of N-ary Tree.
 * Memory Usage: 31.9 MB, less than 100.00% of C++ online submissions for Maximum Depth of N-ary Tree.
 */
