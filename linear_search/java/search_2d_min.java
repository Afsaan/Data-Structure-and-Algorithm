package linear_search.java;

public class search_2d_min {
    public static void main(String[] args){
        int[][] array = {
            {10,21,22},
            {22,100},
            {77,200,80}
        };

        int ans = search_2d_min(array);
        System.out.println(ans);

}


static int search_2d_min(int[][] array){
    int min_value = array[0][0];
    for(int row = 0; row<array.length; row ++){
        for(int column = 0; column<array[row].length; column++){
            if (min_value > array[row][column]){
                min_value = array[row][column];
            }
        }
    }
    return min_value;
}
}
