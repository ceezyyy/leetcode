/**
 * <p>
 * 21. Merge Two Sorted Lists (Easy)
 * https://leetcode.com/problems/merge-two-sorted-lists/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/18
 */
public class MergeTwoLists {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

        ListNode dummy = new ListNode(-1);
        ListNode cur = dummy;

        // Walk through the longest path
        while (l1 != null || l2 != null) {

            // 1) One of the list is null
            if (l1 == null) {
                cur.next = l2;
                break;
            }
            if (l2 == null) {
                cur.next = l1;
                break;
            }

            // 2) Both lists are not null
            if (l1.val <= l2.val) {
                cur.next = new ListNode(l1.val);
                l1 = l1.next;
            } else {
                cur.next = new ListNode(l2.val);
                l2 = l2.next;
            }

            cur = cur.next;

        }

        return dummy.next;

    }
}
