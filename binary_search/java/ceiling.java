public class ceiling {
    public static void main(String[] args) {
        int[] array = {-10,-8,-7,-1, 0, 10,22,23,45,67,78,90,100};
        int tagret = 15;
        System.out.println(ceiling(array, tagret));
    }

    static int ceiling(int[] array, int target){
        int start_point = 0;
        int end_point = array.length - 1;

        while(start_point<=end_point){
            int middle_point = start_point + (end_point-start_point)/2;
            if (array[middle_point] > target){
                end_point = middle_point - 1;
            }else if(array[middle_point] < target){
                start_point = middle_point + 1;
            }else{
                return middle_point;
            }
        }
        return start_point;
    }
}