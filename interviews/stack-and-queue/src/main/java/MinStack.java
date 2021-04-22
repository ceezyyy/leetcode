import java.util.ArrayDeque;
import java.util.Deque;

/**
 * <p>
 * 155. 最小栈 (Easy)
 * https://leetcode-cn.com/problems/min-stack/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/22
 */
class MinStack {

    private Deque<Integer> stack;
    private Deque<Integer> minStack;

    public MinStack() {
        this.stack = new ArrayDeque<>();
        this.minStack = new ArrayDeque<>();
    }

    public void push(int val) {

        // 1) 当 minStack 为空时
        // 2) 当 val 小于等于 minStack 栈顶元素时
        if (minStack.isEmpty() || minStack.peek() >= val) minStack.push(val);

        stack.push(val);

    }

    public void pop() {
        // 当要弹出的元素是 minStack 栈顶元素时
        if (stack.pop().equals(minStack.peek())) minStack.pop();
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return minStack.peek();
    }

}


