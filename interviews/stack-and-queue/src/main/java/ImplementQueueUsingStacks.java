import java.util.ArrayDeque;
import java.util.Deque;

/**
 * <p>
 * 232. Implement Queue using Stacks (Easy)
 * https://leetcode.com/problems/implement-queue-using-stacks/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/22
 */
class ImplementQueueUsingStacks {

    private Deque<Integer> pushStack;
    private Deque<Integer> popStack;


    /**
     * Initialize your data structure here.
     */
    public ImplementQueueUsingStacks() {
        pushStack = new ArrayDeque<>();
        popStack = new ArrayDeque<>();
    }

    /**
     * Push element x to the back of queue.
     */
    public void push(int x) {
        pushStack.push(x);
    }

    /**
     * Removes the element from in front of queue and returns that element.
     */
    public int pop() {

        if (popStack.isEmpty()) {
            // Take it from "pushStack"
            while (!pushStack.isEmpty()) {
                popStack.push(pushStack.pop());
            }
        }

        return popStack.pop();

    }

    /**
     * Get the front element.
     */
    public int peek() {

        if (popStack.isEmpty()) {
            // Take it from "pushStack"
            while (!pushStack.isEmpty()) {
                popStack.push(pushStack.pop());
            }
        }

        return popStack.peek();

    }

    /**
     * Returns whether the queue is empty.
     */
    public boolean empty() {
        return (pushStack.isEmpty() && popStack.isEmpty());
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
