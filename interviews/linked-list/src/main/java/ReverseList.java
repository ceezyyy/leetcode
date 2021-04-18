/**
 * <p>
 * 206. Reverse Linked List (Easy)
 * https://leetcode.com/problems/reverse-linked-list/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/16
 */
public class ReverseList {
    public ListNode reverseList(ListNode head) {

        ListNode pre = null;
        ListNode cur = head;
        ListNode post;

        while (cur != null) {
            post = cur.next;
            cur.next = pre;
            pre = cur;
            cur = post;
        }

        return pre;

    }
}
