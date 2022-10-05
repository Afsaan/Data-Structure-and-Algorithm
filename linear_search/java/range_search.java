package linear_search.java;

// Lets say that we have given an array and we have to search within a range
public class range_search {
    public static void main(String[] args){
        int[] nums = {23,45,1,2,3,6,9,1,10};
        int[] range = {1,4};
        int target = 2;
        int ans = range_search(nums, range, target);
        System.out.println(ans);
    }


    static int range_search(int[] nums, int[] range, int target){
        for(int index = range[0]; index<=range[1]; index++){
            if(nums[index]==target){
                return index;
            }
        }
        return -1;
    }
}
