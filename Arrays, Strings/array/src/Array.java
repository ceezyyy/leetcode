/**
 * CRUD of a fixed size array
 *
 * @author ceezyyy
 */
public class Array {

    private int[] data;

    // the number of elements
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
        this.n = 0;
    }

    /**
     * Get specific element by index
     *
     * @param index
     * @return
     */
    public int get(int index) {
        if (index < 0 || index >= n) return -1;
        return data[index];
    }

    /**
     * Insert an element by specific index
     *
     * @param index
     * @param value
     * @return
     */
    public boolean insert(int index, int value) {
        if (index < 0 || index > n || n == capacity) return false;
        // move elements behind index
        for (int i = n; i > index; i--) {
            data[i] = data[i - 1];
        }
        data[index] = value;
        // Do not forget to increase n by one
        n++;
        return true;
    }


    /**
     * Insert an element
     *
     * @param value
     * @return
     */
    public boolean insert(int value) {
        if (n >= capacity) return false;
        data[n] = value;
        // Do not forget to increase n by one
        n++;
        return true;
    }

    /**
     * Delete an element by specific index
     *
     * @param index
     * @return
     */
    public boolean delete(int index) {
        if (index < 0 || index >= n) return false;
        for (int i = index + 1; i < n; i++) {
            data[i - 1] = data[i];
        }
        // Do not forget to decrease n by one
        --n;
        // zero represent deleted element
        data[n] = 0;
        return true;
    }

    /**
     * Print all elements
     */
    public void printAll() {
        for (int i = 0; i < data.length; i++) {
            System.out.print(data[i]);
            System.out.print(" ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Array myArray = new Array(5);
        // add elements
        for (int i = 0; i < 10; i++) {
            myArray.insert(0, i + 1);
        }
        myArray.printAll();  // 5 4 3 2 1
        // remove elements
        for (int i = 0; i < 5; i++) {
            myArray.delete(0);
        }
        myArray.printAll();  // 0 0 0 0 0
    }

}
