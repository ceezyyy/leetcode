import java.util.ArrayDeque;
import java.util.Deque;

/**
 * <p>
 * 155. Min Stack (Easy)
 * https://leetcode.com/problems/min-stack/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/22
 */
class MinStack {

    // -2^31 <= val <= 2^31 - 1
    private Deque<Integer> stack;
    private Deque<Integer> minStack;

    /**
     * initialize your data structure here.
     */
    public MinStack() {
        stack = new ArrayDeque<>();
        minStack = new ArrayDeque<>();
    }

    public void push(int val) {

        if (minStack.isEmpty() || (!minStack.isEmpty() && val <= minStack.peek())) {
            minStack.push(val);
        }

        stack.push(val);

    }

    public void pop() {
        // Operations will always be called on non-empty stacks.
        if (stack.pop().equals(minStack.peek())) minStack.pop();
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return minStack.peek();
    }

}


