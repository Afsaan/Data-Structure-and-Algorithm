package linear_search.java;

public class maximum_search {
    public static void main(String[] args){
        int[] nums = {23,45,1,2,-3,6,9,1,10};
        int ans = maximum(nums);
        System.out.println(ans);
    }

    static int maximum(int[] nums){
        int max_element = nums[0];
        for(int index=1; index<nums.length; index ++){
            if (max_element<nums[index]){
                max_element = nums[index];
            }
        }
        return max_element;
    }
}

