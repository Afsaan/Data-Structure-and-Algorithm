package linear_search.java;

public class minumun_search {
    public static void main(String[] args){
        int[] nums = {23,45,1,2,-3,6,9,1,10};
        int ans = minimum(nums);
        System.out.println(ans);
    }

    static int minimum(int[] nums){
        int min_element = nums[0];
        for(int index=1; index<nums.length; index ++){
            if (min_element>nums[index]){
                min_element = nums[index];
            }
        }
        return min_element;
    }
}
