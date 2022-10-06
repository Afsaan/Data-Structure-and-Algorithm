package linear_search.java;

public class search_2d_max {
    public static void main(String[] args){
        int[][] array = {
            {10,21,22},
            {22,100},
            {77,200,80}
        };

        int ans = search_2d_max(array);
        System.out.println(ans);

}


static int search_2d_max(int[][] array){
    int max_value = array[0][0];
    for(int row = 0; row<array.length; row ++){
        for(int column = 0; column<array[row].length; column++){
            if (max_value < array[row][column]){
                max_value = array[row][column];
            }
        }
    }
    return max_value;
}
}
