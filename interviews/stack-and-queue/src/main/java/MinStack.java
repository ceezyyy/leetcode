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

    private Deque<Integer> stack;
    private Deque<Integer> minStack;

    public MinStack() {
        this.stack = new ArrayDeque<>();
        this.minStack = new ArrayDeque<>();
    }

    public void push(int val) {
        /*
          1) 当 minStack 为空时
          2) 当 val 小于等于 minStack 栈顶元素
         */
        if (minStack.isEmpty() || minStack.peek() >= val) minStack.push(val);
        stack.push(val);

    }

    public void pop() {
        // 当即将弹出的元素等于 minStack 栈顶元素
        if (stack.pop().equals(minStack.peek())) minStack.pop();
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        // 符合 LIFO, 查找 O(1)
        return minStack.peek();
    }

}


