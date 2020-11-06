# Solve Tree Problems Recursively

Table of Contents
-----------------

* [Overview](#overview)
* [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
* [Symmetric Tree](#symmetric-tree)
* [Path Sum](#path-sum)
* [Invert Binary Tree](#invert-binary-tree)

## Overview

本文研究采用递归思想破解二叉树相关题目

- 明确函数的定义，不要跳进递归细节，即搞清楚 `root` 节点它自己要做什么（巧用辅助函数，传递参数）
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

当前 `root` 的工作：需要获取左右孩子中最大的深度且加 1（`bottom-up` 自底向上）

边界条件：当 `root` 为空时，返回 0（深度为 0）



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

当前 `root` 的工作：与镜子中的自己相比较（因为比较是对于两个物体的，所以需要借助辅助函数 `isMirror()`，并传递两个参数）



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

当前 `root` 的工作（不是叶子节点）：将当前的 `sum` 值更新（减去当前自己的 `val`），并判断左右孩子是否满足条件（递归）

当前 `root` 的工作（是叶子结点）：判断当前的 `sum` 值是否等于自己的 `val`，若是，返回 `true`

边界条件：返回 `false`（当叶子节点 / 该路径不满足条件时才走到这一层）



**Solution.java**

```java
/**
 * Path Sum
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    public boolean hasPathSum(TreeNode root, int sum) {

        // Corner case
        if (root == null) return false;

        // Leaf
        if (root.left == null && root.right == null && sum == root.val) {
            return true;
        }

        return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);

    }
}
```



## Invert Binary Tree

**Example**

Input:

```
     4
   /   \
  2     7
 / \   / \
1   3 6   9
```

Output:

```
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```



**Explained**

当前 `root` 的工作：交换自己的左右孩子，**且分别对左右孩子进行反转**

边界条件：返回 `null`



**Solution.java**

```java
/**
 * Invert Binary Tree
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    public TreeNode invertTree(TreeNode root) {

        if (root == null) return null;

        // Swap children
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;

        invertTree(root.left);
        invertTree(root.right);

        return root;

    }
}
```

