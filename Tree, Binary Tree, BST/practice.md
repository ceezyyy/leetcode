# Practice for Binary Tree

Table of Contents
-----------------

* [Overview](#overview)
* [Populating Next Right Pointers in Each Node](#populating-next-right-pointers-in-each-node)


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