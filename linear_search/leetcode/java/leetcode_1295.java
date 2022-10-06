package linear_search.java;
public class leetcode_1295{
    public static void main(String[] args){
       int[] nums = {12,345,0,6,7896};

       System.out.println(even_digit(nums));
    }

    static int even_digit(int[] nums){
        int count = 0;
        for(int num: nums){
            if (even(num)){
                count ++;
            }
        }
        return count;
    }

    static boolean even(int num){
        if (num < 0){
            num = num * -1;
        }

        if (num==0){
            return false;
        }

        int output = count_digit(num);
        return output %2 ==0;

    }

    static int count_digit(int num){
        int count = 0;
        while(num>0){
            count ++;
            num = num / 10;
        }
        return count;
    }
}