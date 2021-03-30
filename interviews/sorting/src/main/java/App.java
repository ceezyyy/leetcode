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

//        int[] arr = new int[]{3, 4, 1, 32, 0, 1, 5,  12, 2, 5, 7, 8, 9, 2, 44, 111, 5};

        int[] arr = new int[]{1, -1, 2, 0   };
        QuickSort.sort(arr, 0, arr.length - 1);

        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            System.out.print(" ");
        }

    }

}
