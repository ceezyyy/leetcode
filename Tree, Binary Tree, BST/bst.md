# BST

Table of Contents
-----------------

* [Overview](#overview)
* [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)
* [Convert BST to Greater Tree](#convert-bst-to-greater-tree)




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

