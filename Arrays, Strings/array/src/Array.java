/**
 * CRUD of a fixed size array
 *
 * @author ceezyyy
 */
public class Array {

    private int[] data;
    private int n;
    private int capacity;

    /**
     * Initialize an array
     *
     * @param capacity
     */
    public Array(int capacity) {
        int[] data = new int[capacity];
        this.data = data;
        this.capacity = capacity;
    }

    /**
     * Get specific element by index
     *
     * @param index
     * @return
     */
    public int findByIndex(int index) {
        return 0;
    }

    /**
     * Insert an element by specific index
     *
     * @param index
     * @param value
     * @return
     */
    public boolean insert(int index, int value) {
        return true;
    }

    /**
     * Delete an element by specific index
     *
     * @param index
     * @return
     */
    public boolean delete(int index) {
        return true;
    }

    /**
     * Print all elements
     */
    public void printAll() {
        for (int i = 0; i < data.length; i++) {
            System.out.println(data[i]);
        }
    }

    public static void main(String[] args) {


    }

}
