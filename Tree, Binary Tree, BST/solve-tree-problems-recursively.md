# Solve Tree Problems Recursively

Table of Contents
-----------------

* [Overview](#overview)
* [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
* [Symmetric Tree](#symmetric-tree)
* [Path Sum](#path-sum)


## Overview

本文研究采用递归思想破解二叉树相关题目

- 明确函数的定义，不要跳进递归细节，即搞清楚`root` 节点它自己要做什么（巧用辅助函数，传递参数）
- 根据题目特点选择前序（`top-down`），中序，后序（`bottom-up`）递归框架



## Maximum Depth of Binary Tree

**Example:**

Given binary tree `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

return its depth = 3.



**Explained**

对于每个节点来讲，只需要获取左右孩子中最大的深度，再累加 1 即可（从子节点获取最大深度，可采用 `bottom-up` 思想 ）

当节点为空时，返回 0



**Solution.java**

```java
/**
 * Maximum Depth of Binary Tree
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    // Bottom-up
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }
}
```



## Symmetric Tree

**Example**

This binary tree `[1,2,2,3,4,4,3]` is symmetric:

```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```

But the following `[1,2,2,null,3,null,3]` is not:

```
    1
   / \
  2   2
   \   \
   3    3
```

**Explained**



<div align="center"> <img src="mirror_1.png" width="20%"/> </div><br>

<div align="center"> <img src="mirror_2.png" width="30%"/> </div><br>



**Solution.java**

```java
/**
 * Symmetric Tree
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;f
        TreeNode right;
    }

    public boolean isSymmetric(TreeNode root) {
        return isMirror(root, root);
    }

    // Top-down
    public boolean isMirror(TreeNode n1, TreeNode n2) {
        // Corner cases
        if (n1 == null && n2 == null) return true;
        if (n1 == null || n2 == null) return false;
        
        return (n1.val == n2.val) && isMirror(n1.left, n2.right) && isMirror(n1.right, n2.left);
    }

}
```



## Path Sum

**Example**

Given the below binary tree and `sum = 22`,

```
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
```

return true, as there exist a root-to-leaf path `5->4->11->2` which sum is 22.

**Explained**

