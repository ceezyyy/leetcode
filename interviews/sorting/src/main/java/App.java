/**
 * <p>
 * 排序算法测试类
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/26
 */
public class App {
    public static void main(String[] args) {

        int[] arr = new int[]{4, 23, 6, 78, 1, 54, 231, 9, 12, 923829382, 989, 11, -1};

        arr = SelectionSort.sort(arr);

        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            System.out.print(" ");
        }

    }
}
