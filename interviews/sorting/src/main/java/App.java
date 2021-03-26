/**
 * <p>
 *
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/26
 */
public class App {
    public static void main(String[] args) {

        int[] arr = new int[]{4, 23, 6, 78, 1, 54, 231, 9, 12, 8989800, -1232, 89, 0};

        MergeSort.sort(arr, 0, arr.length - 1);

        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            System.out.print(" ");
        }

    }

}
