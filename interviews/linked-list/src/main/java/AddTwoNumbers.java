/**
 * <p>
 * 2. Add Two Numbers (Medium)
 * https://leetcode.com/problems/add-two-numbers/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/16
 */
class AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        /*
          Why dummy?
          handling corner cases perfectly
         */
        ListNode dummy = new ListNode(-1);
        ListNode cur = dummy;
        int sum = 0;

        /*
          Walk through the longest path
          instead of merging
         */
        while (l1 != null || l2 != null) {

            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }

            cur.next = new ListNode(sum % 10);
            cur = cur.next;

            /*
              Update "carry"
              only two choices: 0 or 1
             */
            sum /= 10;

        }

        if (sum == 1) cur.next = new ListNode(1);
        return dummy.next;

    }
}
