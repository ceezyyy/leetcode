/**
 * <p>
 * 61. Rotate List (Medium)
 * https://leetcode.com/problems/rotate-list/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/19
 */
public class RotateList {
    public ListNode rotateRight(ListNode head, int k) {

        // Corner case
        if (head == null || k == 0) return head;

        int n = 0;
        int steps = 0;
        ListNode dummy = new ListNode(-1);
        ListNode cur = head;
        dummy.next = head;

        // 1. 遍历, 获取 n
        while (cur != null) {
            cur = cur.next;
            n++;
        }

        // 2. 找到链, 用 dummy 指向
        k = k % n;
        if (k == 0) return head;
        steps = n - k - 1;
        cur = head;
        while (steps-- > 0) {
            cur = cur.next;
        }
        dummy.next = cur.next;
        cur.next = null;

        // 3. 找到链的尾巴, 指向原来的 head
        cur = dummy;
        while (cur.next != null) {
            cur = cur.next;
        }
        cur.next = head;

        return dummy.next;

    }
}
