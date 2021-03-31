/**
 * <p>
 * 1315. Sum of Nodes with Even-Valued Grandparent (Medium)
 * https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/31
 */
public class SumEvenGrandparent {

    private int res = 0;

    public int sumEvenGrandparent(TreeNode root) {

        /*
          The value of nodes is between 1 and 100
          so, -1 represents null
         */
        preorder(root, -1, -1);
        return res;
    }

    public void preorder(TreeNode root, int parent, int grandParent) {

        if (root == null) return;

        if (grandParent != -1 && grandParent % 2 == 0) res += root.val;

        preorder(root.left, root.val, parent);
        preorder(root.right, root.val, parent);

    }
}
