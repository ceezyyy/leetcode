# BST

Table of Contents
-----------------

* [Overview](#overview)
* [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)
* [Convert BST to Greater Tree](#convert-bst-to-greater-tree)
* [Validate Binary Search Tree](#validate-binary-search-tree)
* [Search in a Binary Search Tree](#search-in-a-binary-search-tree)
* [Insert into a Binary Search Tree](#insert-into-a-binary-search-tree)
* [Count Complete Tree Nodes](#count-complete-tree-nodes)
* [References](#references)



## Overview







## Kth Smallest Element in a BST

**Example 1**

```
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
```

**Example 2**

```
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
```



**Follow up**
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?



**Explained**











**Solution.java**

```java
/**
 * Kth Smallest Element in a BST
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

    }

    public List<Integer> elements = new ArrayList<>();

    public int kthSmallest(TreeNode root, int k) {
        // The number of elements of the BST is between 1 to 10^4
        inorder(root);
        // You may assume k is always valid, 1 ≤ k ≤ BST's total elements
        return elements.get(k - 1);
    }

    public void inorder(TreeNode root) {
        // Corner case
        if (root == null) {
            return;
        }
        inorder(root.left);
        elements.add(root.val);
        inorder(root.right);
    }
}
```

## Convert BST to Greater Tree

**Example**



<div align="center"> <img src="538.png" width="50%"/> </div><br>


```
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null
```

**Explained**



**Solution.java**

```java
/**
 * Convert BST to Greater Tree
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    private int sum = 0;

    public TreeNode convertBST(TreeNode root) {
        calculateBST(root);
        return root;
    }

    public void calculateBST(TreeNode root) {

        // Corner case
        if (root == null) return;

        calculateBST(root.right);
        // Key point
        sum += root.val;
        root.val = sum;
        calculateBST(root.left);

    }
}
```





## Validate Binary Search Tree

**Example**

```
    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```



**Explained**









**Solution.java**

```java
/**
 * Validate Binary Search Tree
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    public boolean isValidBST(TreeNode root) {

        // Corner case
        if (root == null) return true;

        // Use Long instead of Integer
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);

    }

    public boolean isValidBST(TreeNode root, long min, long max) {

        // Corner case
        if (root == null) return true;

        // Root: -inf < root < inf
        // Left subtree: -inf < left < root
        // Right subtree: root < right < inf
        int val = root.val;
        if (val >= max || val <= min) return false;

        return isValidBST(root.left, min, val) && isValidBST(root.right, val, max);

    }
}
```





## Search in a Binary Search Tree

**Example**

```
Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
```

You should return this subtree:

```
      2     
     / \   
    1   3
```



**Explained**





**Solution.java**

```java
/**
 * Search in a Binary Search Tree
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    public TreeNode searchBST(TreeNode root, int val) {

        // Corner case
        if (root == null) return null;

        // Bingo
        if (root.val == val) return root;

        if (val < root.val) {
            return searchBST(root.left, val);
        } else {
            return searchBST(root.right, val);
        }

    }
}
```



## Insert into a Binary Search Tree

**Example**



<div align="center"> <img src="insert_bst.jpg" width="50%"/> </div><br>


```
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
```

**Explained**





**Solution.java**

```java
/**
 * Insert into a Binary Search Tree
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

    public TreeNode insertIntoBST(TreeNode root, int val) {

        if (root == null) return new TreeNode(val);

        // It's guaranteed that val does not exist in the original BST
        if (val < root.val) {
            root.left = insertIntoBST(root.left, val);
        } else {
            root.right = insertIntoBST(root.right, val);
        }

        return root;

    }
}
```



## Count Complete Tree Nodes









## References

- [Check if Binary Tree is Binary Search Tree](https://www.youtube.com/watch?v=MILxfAbIhrE)

