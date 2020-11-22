# Practices for Binary Tree

Table of Contents
-----------------

* [Overview](#overview)
* [Populating Next Right Pointers in Each Node](#populating-next-right-pointers-in-each-node)
* [Maximum Binary Tree](#maximum-binary-tree)
* [Construct Binary Tree from Preorder and Inorder Traversal](#construct-binary-tree-from-preorder-and-inorder-traversal)
* [Construct Binary Tree from Inorder and Postorder Traversal](#construct-binary-tree-from-inorder-and-postorder-traversal)
* [Serialize and Deserialize Binary Tree](#serialize-and-deserialize-binary-tree)
* [Univalued Binary Tree](#univalued-binary-tree)




## Overview

二叉树递归思维训练合集

## Populating Next Right Pointers in Each Node

**Example**



<div align="center"> <img src="116_sample.png" width="50%"/> </div><br>




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

## Construct Binary Tree from Preorder and Inorder Traversal

**Example**

For example, given

```
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
```

Return the following binary tree:

```
    3
   / \
  9  20
    /  \
   15   7
```



**Explained**

当前 `root` 的工作: 构建新的 `root`，以及确定自己的左右孩子



我们首先得明确三点：

1. 前序遍历： `root` 永远在第一位
2. 中序遍历：根据 `root` 可以分为左右子树
3. 后序遍历： `root` 永远在最后一位



根据这个知识，我们可以利用一个变量记录 `root` 的索引（根据前序遍历结果），接着在中序遍历结果找到当前的 `root`（题目说明元素不重复），将其分为左右两个区间（左右子树），递归调用





**Solution.java**

```java
/**
 * Construct Binary Tree from Preorder and Inorder Traversal
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int val) {
            this.val = val;
        }
    }

    public TreeNode buildTree(int[] preorder, int[] inorder) {

        // Corner case
        if (preorder == null || preorder.length == 0 || preorder.length != inorder.length) return null;

        // Duplicates do not exist in the tree
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < preorder.length; i++) {
            map.put(inorder[i], i);
        }

        return buildTree(preorder, inorder, 0, 0, preorder.length - 1, map);

    }

    // Preorder: Determine where the root at
    // Inorder: Determine the left & right interval
    public TreeNode buildTree(int[] preorder, int[] inorder,
                              int preIndex,
                              int inStart, int inEnd,
                              Map<Integer, Integer> map) {

        // Corner case
        if (inStart > inEnd || preIndex < 0 || preIndex >= preorder.length) return null;

        TreeNode root = new TreeNode(preorder[preIndex]);

        // Dividing line: left root right
        int inIndex = map.get(preorder[preIndex]);
        root.left = buildTree(preorder, inorder, preIndex + 1, inStart, inIndex - 1, map);
        // (inIndex - inStart) represents how many nodes in left subtree
        root.right = buildTree(preorder, inorder, preIndex + (inIndex - inStart) + 1, inIndex + 1, inEnd, map);

        return root;

    }
}
```







## Construct Binary Tree from Inorder and Postorder Traversal

**Example**

For example, given

```
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
```

Return the following binary tree:

```
    3
   / \
  9  20
    /  \
   15   7
```

**Explained**

看上题，换汤不换药



**Solution.java**

```java
/**
 * Construct Binary Tree from Inorder and Postorder Traversal
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int val) {
            this.val = val;
        }
    }

    public TreeNode buildTree(int[] inorder, int[] postorder) {

        // Corner case
        if (inorder == null || inorder.length == 0 || inorder.length != postorder.length) return null;

        // Duplicates do not exist in the tree
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            map.put(inorder[i], i);
        }

        return buildTree(inorder, postorder, postorder.length - 1, 0, inorder.length - 1, map);

    }

    // Postorder: Determine where the root at
    // Inorder: Determine the left & right interval
    public TreeNode buildTree(int[] inorder, int[] postorder,
                              int postIndex,
                              int inStart, int inEnd,
                              Map<Integer, Integer> map) {

        // Corner case
        if (inStart > inEnd || postIndex >= postorder.length || postIndex < 0) return null;

        TreeNode root = new TreeNode(postorder[postIndex]);

        // Dividing line: left root right
        int inIndex = map.get(postorder[postIndex]);
        root.right = buildTree(inorder, postorder, postIndex - 1, inIndex + 1, inEnd, map);
        // (inEnd - inIndex) represents how many nodes in right subtree
        root.left = buildTree(inorder, postorder, postIndex - (inEnd - inIndex) - 1, inStart, inIndex - 1, map);

        return root;

    }
}
```



## Serialize and Deserialize Binary Tree

**Example**

<div align="center"> <img src="se_de.jpg" width="20%"/> </div><br>

```
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
```





**Explain**



**Codec.java**

```java
/**
 * Serialize and Deserialize Binary Tree
 */
public class Codec {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int val) {
            this.val = val;
        }
    }

    private StringBuilder result = new StringBuilder();

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        buildString(root);
        return result.toString();
    }

    public void buildString(TreeNode root) {

        // Corner case
        if (root == null) {
            result.append("null").append(",");
            // Do not forget to return
            return;
        }

        result.append(String.valueOf(root.val)).append(",");
        buildString(root.left);
        buildString(root.right);

    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {

        // String[] -> Deque
        List<String> nodes = Arrays.asList(data.split(","));
        Deque<String> elements = new ArrayDeque<>(nodes);
        return buildTree(elements);

    }

    public TreeNode buildTree(Deque<String> elements) {

        // Corner case
        if (elements == null) return null;

        String val = elements.remove();

        // Do not use "=="
        if ("null".equals(val)) return null;

        TreeNode root = new TreeNode(Integer.parseInt(val));
        root.left = buildTree(elements);
        root.right = buildTree(elements);

        return root;

    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));
```



## Univalued Binary Tree

**Example**

<div align="center"> <img src="unival.png" width="20%"/> </div><br>



```
Input: [2,2,2,5,2]
Output: false
```

**Explained**

**Solution.java**

```java
/**
 * Univalued Binary Tree
 * <p>
 * A binary tree is univalued if every node in the tree has the same value.
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    public boolean isUnivalTree(TreeNode root) {
        // The number of nodes in the given tree will be in the range [1, 100]
        return isUnivalTree(root, root.val);
    }

    public boolean isUnivalTree(TreeNode root, int val) {

        // Corner case
        if (root == null) return true;

        if (root.val != val) return false;

        return isUnivalTree(root.left, val) && isUnivalTree(root.right, val);

    }
}
```