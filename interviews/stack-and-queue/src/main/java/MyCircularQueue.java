/**
 * <p>
 * 622. 设计循环队列 (Medium)
 * https://leetcode-cn.com/problems/design-circular-queue/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/23
 */
class MyCircularQueue {

    private int n;
    private int[] data;
    // 实际元素的个数, 可以方便判空/满
    private int size;
    // 头指针, 初始化为 0
    private int head;

    public MyCircularQueue(int k) {
        this.n = k;
        this.data = new int[n];
        size = 0;
        head = 0;
    }

    public boolean enQueue(int value) {

        if (isFull()) return false;

        // 先移动尾指针, 再更新
        int tail = (head + size - 1) % n;
        tail = (tail + 1) % n;
        data[tail] = value;
        size++;

        return true;

    }

    public boolean deQueue() {

        if (isEmpty()) return false;

        // 先更新, 再移动头指针
        data[head] = -1;
        head = (head + 1) % n;
        size--;

        return true;

    }

    public int Front() {
        return isEmpty() ? -1 : data[head];
    }

    public int Rear() {
        // 计算尾指针
        return isEmpty() ? -1 : data[(head + size - 1) % n];
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == n;
    }

}
