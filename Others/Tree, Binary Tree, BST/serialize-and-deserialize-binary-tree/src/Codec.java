import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.List;

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