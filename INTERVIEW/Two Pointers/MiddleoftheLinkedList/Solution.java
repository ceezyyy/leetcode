/**
 * @Topic 876. Middle of the Linked List
 * @Author Yi Cai
 * @Tag Two Pointers
 * @Date 3/25/2020 6:31 PM
 **/


class Solution {
    public ListNode middleNode(ListNode head) {
        // Slow pointer & Fast pointer
        ListNode slow = head;
        ListNode fast = head;

        // Slow pointer: move one step
        // Fast pointer: move two steps
        while (fast != null && fast.next != null) {  // Avoid NullPointerException
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}


// Time Complexity: O(n)
// Space Complexity: O(1)

