# Solve Tree Problems Recursively

Table of Contents
-----------------

* [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
* [Symmetric Tree](#symmetric-tree)
* [Path Sum](#path-sum)
* [References](#references)



## Explained

```
1. return specific value for null node
2. update the answer if needed                      // answer <-- params
3. left_ans = top_down(root.left, left_params)      // left_params <-- root.val, params
4. right_ans = top_down(root.right, right_params)   // right_params <-- root.val, params 
5. return the answer if needed                      // answer <-- left_ans, right_ans
```







```
return if root is null
2. if root is a leaf node:
3.      answer = max(answer, depth)         // update the answer if needed
4. maximum_depth(root.left, depth + 1)      // call the function recursively for left child
5. maximum_depth(root.right, depth + 1)     // call the function recursively for right child
```






## Maximum Depth of Binary Tree

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









## Path Sum







## References