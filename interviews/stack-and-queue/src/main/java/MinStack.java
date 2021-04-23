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
        /*
          1) minStack 为空时, 直接加入
          2) 维持不递增 minStack
         */
        if (minStack.isEmpty() || minStack.peek() >= val) minStack.push(val);
        stack.push(val);

    }

    public void pop() {
        // 更新 minStack
        if (stack.pop().equals(minStack.peek())) minStack.pop();
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        // 查找 O(1)
        return minStack.peek();
    }

}


