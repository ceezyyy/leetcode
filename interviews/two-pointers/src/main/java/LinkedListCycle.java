/**
 * <p>
 * 141. Linked List Cycle
 * https://leetcode.com/problems/linked-list-cycle/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/24
 */
public class LinkedListCycle {
    public boolean hasCycle(ListNode head) {

        if (head == null || head.next == null) return false;

        /*
          a is "walker"
          b is "runner"

          e.g: two guys are racing in a circular playground
          one's speed is twice as the other, if they start at
          the same time, they are bound to meet
         */
        ListNode a = head;
        ListNode b = head;

        /*
          Do not forget to determine if "b.next" is null
         */
        while (b.next != null && b.next.next != null) {

            a = a.next;
            b = b.next.next;

            if (a == b) return true;

        }

        return false;

    }
}
