package linear_search.leetcode.java;

import javax.sound.sampled.SourceDataLine;

public class leetcdoe_1672 {
    public static void main(String[] args){
        int[][] accounts = {{1,2,3},{1,2}};

        int ans = max_wealth(accounts);
        System.out.println(ans);
     }
    
     static int max_wealth(int[][] accounts){
        int max_wealth = 0;
        for(int row = 0; row<accounts.length; row++){
            int sum = 0;
            for(int column=0; column<accounts[row].length; column++){
                sum = sum + accounts[row][column];
            }
            if(max_wealth<sum){
                max_wealth = sum;
            }
        }
        return max_wealth;
    }
}
