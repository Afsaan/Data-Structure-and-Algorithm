package linear_search.java;
public class Main{
    public static void main(String[] args){
        int[] nums = {23,45,1,2,3,6,9,1,10};
        int target = 9;
        int ans = linear_search(nums, target);
        System.out.println(ans);
    }

    // search in the array: return index if item found else -a
    static int linear_search(int[] arr, int target){
        for (int index=0; index<arr.length; index++){
            if (target == arr[index]){
                return index;
            }
        }
        return -1;
    }
}