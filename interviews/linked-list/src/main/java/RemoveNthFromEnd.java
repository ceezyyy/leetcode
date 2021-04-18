/**
 * <p>
 * 19. Remove Nth Node From End of List (Medium)
 * https://leetcode.com/problems/remove-nth-node-from-end-of-list/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/16
 */
public class RemoveNthFromEnd {
    public ListNode removeNthFromEnd(ListNode head, int n) {

        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode cur = head;
        int size = 0;
        int steps = 0;

        // Get the size
        while (cur != null) {
            cur = cur.next;
            size++;
        }

        // The relationship between size and n-th from the end
        steps = size - n;
        cur = dummy;

        while (steps-- > 0) cur = cur.next;
        cur.next = cur.next.next;

        return dummy.next;

    }
}
