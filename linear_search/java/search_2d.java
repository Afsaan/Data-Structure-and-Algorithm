package linear_search.java;
import java.util.Arrays;

public class search_2d {
    public static void main(String[] args){
            int[][] array = {
                {10,21,22},
                {22,100},
                {77,200,80}
            };

            int target = 200;
            int[] ans = search_2d(array, target);
            System.out.println(Arrays.toString(ans));

    }


    static int[] search_2d(int[][] array, int target){
        for(int row = 0; row<array.length; row ++){
            for(int column = 0; column<array[row].length; column++){
                if (array[row][column] == target){
                    return new int[]{row,column};
                }
            }
        }
        return new int[]{-1,-1};
    }
}

