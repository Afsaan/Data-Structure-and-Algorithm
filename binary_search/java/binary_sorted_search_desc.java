package binary_search.java;

public class binary_sorted_search_desc {
    public static void main(String[] args) {
        int[] array = {800,700,78,67,56,45,34,23,12,11};
        int tagret = 700;
        System.out.println(binary_search(array, tagret));
    }

    static int binary_search(int[] array, int target){
        int start_point = 0;
        int end_point = array.length - 1;

        while(start_point<=end_point){
            int middle_point = start_point + (end_point-start_point)/2;
            if (array[middle_point] < target){
                end_point = middle_point - 1;
            }else if(array[middle_point] > target){
                start_point = middle_point + 1;
            }else{
                return middle_point;
            }
        }
        return -1;
    }
}
