public class Main {

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next = new ListNode(3);
        head.next = new ListNode(4);
        head.next = new ListNode(5);
        head.next = new ListNode(6);

        Solution solution = new Solution();
        ListNode result = solution.middleNode(head);
        System.out.println(result);
    }
}
