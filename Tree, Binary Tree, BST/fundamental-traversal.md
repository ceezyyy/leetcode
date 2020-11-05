# Fundamental Traversal

Table of Contents
-----------------

* [Explained](#explained)
* [Preorder](#preorder)
* [Inorder](#inorder)
* [Postorder](#postorder)
* [References](#references)

## Explained

> 二叉树拥有天然的递归结构



<div align="center"> <img src="binary_tree.png" width="30%"/> </div><br>

二叉树遍历问题分三种情况：

- Preorder: **n** l r
- Inorder: l **n** r
- Postorder: l r **n**

`n` 为根节点，`l` 为左节点，`r` 为右节点



举个例子前序遍历的例子，

对于每个节点都遵循着同一个 `policy`：（中序遍历和后序遍历同理，只是顺序的差异）

“轮到我了，我上！（将自己的值输出），接下来到我的左孩子，然后右孩子”



**每个节点都重复做着相同的事情 / 判断，一直循环下去，直到不满足某一条件，这就是递归的思想**



## Preorder

```java
/**
 * Binary Tree Preorder Traversal
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    private List<Integer> result = new LinkedList<>();

    public List<Integer> preorderTraversal(TreeNode root) {
        pre(root);
        return result;
    }

    public void pre(TreeNode node) {
        if (node == null) return;
        result.add(node.val);
        pre(node.left);
        pre(node.right);
    }

} 
```



## Inorder

```java
/**
 * Binary Tree Inorder Traversal
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    private List<Integer> result = new LinkedList<>();

    public List<Integer> inorderTraversal(TreeNode root) {
        in(root);
        return result;
    }

    public void in(TreeNode node) {
        if (node == null) return;
        in(node.left);
        result.add(node.val);
        in(node.right);
    }

}
```



## Postorder

```java
/**
 * Binary Tree Postorder Traversal
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    private List<Integer> result = new LinkedList<>();

    public List<Integer> postorderTraversal(TreeNode root) {
        post(root);
        return result;
    }

    public void post(TreeNode node) {
        if (node == null) return;
        post(node.left);
        post(node.right);
        result.add(node.val);
    }

}
```



## References

- [学习算法和刷题的框架思维 - labuladong](https://labuladong.gitbook.io/algo/di-ling-zhang-bi-du-xi-lie-qing-an-shun-xu-yue-du/xue-xi-shu-ju-jie-gou-he-suan-fa-de-gao-xiao-fang-fa)
- [Binary Tree Bootcamp: Full, Complete, & Perfect Trees. Preorder, Inorder, & Postorder Traversal.](https://www.youtube.com/watch?v=BHB0B1jFKQc&t=177s)

