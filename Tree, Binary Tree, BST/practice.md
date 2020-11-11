# Practice for Binary Tree

Table of Contents
-----------------

* [Overview](#overview)
* [Populating Next Right Pointers in Each Node](#populating-next-right-pointers-in-each-node)
* [Maximum Binary Tree](#maximum-binary-tree)



## Overview

二叉树递归思维训练合集

## Populating Next Right Pointers in Each Node

**Example**



<div align="center"> <img src="116_sample.png" width="60%"/> </div><br>




```
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
```



**Explained**

当前 `root` 的工作: 1.将自己的左右孩子连接 2.将跨父节点的两个字节点连接（思考问题时只看二叉树前三层）

边界条件: `root` 为空时直接返回（二叉树问题经常要判空!）



**Solution.java**

```java
/**
 * Populating Next Right Pointers in Each Node
 */
class Solution {

    public class Node {
        public int val;
        public Node left;
        public Node right;
        public Node next;
    }

    public Node connect(Node root) {
        if (root == null) return root;
        connect(root.left, root.right);
        return root;
    }

    public void connect(Node left, Node right) {

        if (left == null || right == null) return;

        left.next = right;
        right.next = null;

        connect(left.left, left.right);
        connect(left.right, right.left);
        connect(right.left, right.right);

    }
}
```



## Maximum Binary Tree

**Example**


```
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
```



**Explained**





**Solution.java**

```java
/**
 * Maximum Binary Tree
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public TreeNode constructMaximumBinaryTree(int[] nums) {
        // Corner case
        if (nums == null || nums.length == 0) return null;
        return constructMaximumBinaryTree(nums, 0, nums.length);
    }

    // [left, right) interval
    public TreeNode constructMaximumBinaryTree(int[] nums, int left, int right) {

        // Corner case
        if (left >= right) return null;

        // Recursively
        int indexOfMax = getIndexOfMax(nums, left, right);
        TreeNode root = new TreeNode(nums[indexOfMax]);
        root.left = constructMaximumBinaryTree(nums, left, indexOfMax);
        root.right = constructMaximumBinaryTree(nums, indexOfMax + 1, right);

        return root;

    }

    public int getIndexOfMax(int[] nums, int left, int right) {
        int index = left;
        for (int i = left + 1; i < right; i++) {
            if (nums[i] > nums[index]) {
                index = i;
            }
        }
        return index;
    }
}
```