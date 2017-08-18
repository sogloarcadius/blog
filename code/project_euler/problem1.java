import java.util.ArrayList;

public class Problem1 {
    
  
    public static void main (String[] args ) {
       
       int n=10;
       ArrayList<Integer> multiples_of_3_or_5 = new ArrayList<Integer>();
       int sum_multiples_of_3_or_5 = 0;
        
        for (int number=0; number < n; number++){
            
            if ( isMultiple3or5(number) == true) {
                
                multiples_of_3_or_5.add(number);
                sum_multiples_of_3_or_5+=number;
            }
  
        }
        
        System.out.println(multiples_of_3_or_5.toString());
        System.out.println(sum_multiples_of_3_or_5);
  
    }
    
    
    static Boolean isMultiple3or5(int number) {

        if ( number % 3 == 0 || number % 5 == 0 ){ 
            return true;
        } else {
            return false;
        }
    }
}
    
    