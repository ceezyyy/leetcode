/**
 * <p>
 * 160. Intersection of Two Linked Lists (Easy)
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/22
 */
public class GetIntersectionNode {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {

        if (headA == null || headB == null) return null;
        ListNode a = headA;
        ListNode b = headB;

        /*
          If two lists have intersection:
            1) c is the common part
            2) A: a + c
            3) B: b + c
            so A + b = B + a, they will meet at the intersection
          If no intersection:
            1) A: a
            2) B: b
            so A + b = B + a, they will both meet the end of the list ("null")
         */
        while (a != b) {
            a = a == null ? headB : a.next;
            b = b == null ? headA : b.next;
        }

        return a;

    }
}
