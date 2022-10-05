package linear_search.java;
public class Main{
    public static void main(String[] args){
        String str = "afsan khan";
        char target = 'f';
        int ans = string_search(str, target);
        System.out.println(ans);
    }

    // search in the array: return index if item found else -a
    static int string_search(String str, char target){
        for (int index=0; index<str.length(); index++){
            if (target == str.charAt(index)){
                return index;
            }
        }
        return -1;
    }
}