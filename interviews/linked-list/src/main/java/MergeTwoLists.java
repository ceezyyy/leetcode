/**
 * <p>
 * 21. 合并两个有序链表 (Easy)
 * https://leetcode-cn.com/problems/merge-two-sorted-lists/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/18
 */
public class MergeTwoLists {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

        ListNode dummy = new ListNode(-1);
        ListNode cur = dummy;

        while (l1 != null || l2 != null) {

            // 一方为空, 则指向另一方, 结束
            if (l1 == null) {
                cur.next = l2;
                break;
            }
            if (l2 == null) {
                cur.next = l1;
                break;
            }

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
