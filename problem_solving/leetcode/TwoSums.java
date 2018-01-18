// Java implementation of Two Sum
import java.util.List;
import java.util.ArrayList;

public class TwoSums {

     
    public static void main (String args[]){
       
    
        ArrayList<int[]> result = new ArrayList<int[]>();
        result.addAll(AllTwoSums(new int[]{1, 2, 3, 4, 5,7,8,9,10,11,12,13}, 12));
        
        
        for (int [] element : result){
            System.out.print("[");
            for (int i=0; i<element.length; i++){
                System.out.print(element[i] + " ");
            }
            System.out.print("]" + "\t");

        }
        
        /*
        int[] result = TwoSums(new int[]{2, 7, 11, 15}, 9);
    
        for (int i=0; i<result.length; i++){
            
            System.out.println(result[i]);
        };
        */
        
    }
    
    
    public static ArrayList<int[]> AllTwoSums(int[] numbers, int target) {
        
        
        ArrayList<int[]> result = new ArrayList<int[]>();
        
        for (int i=0; i <numbers.length; i++){
            
            for (int j=i+1; j <numbers.length; j++){
                
                if (numbers[i] + numbers[j] == target){
                    
                    result.add(new int[]{i,j});
                }
            }
        }
        
        return result;
        
    }
    
    public static int[] TwoSums(int[] numbers, int target){
    
        int[] result = new int[2];
        int currentIndice = 0;
        boolean flag = false;
        
        while ( currentIndice < numbers.length & flag == false  ){
            
            int j=currentIndice+1;
            
            while (j < numbers.length & flag == false){
                
                if ( numbers[currentIndice] + numbers[j] == target) {

                    result[0]=currentIndice;
                    result[1]=j;
                    flag = true;
                }
                
                j=j+1;
            }
            currentIndice=currentIndice+1;
        }
        
        return result;
    }
}
            
            
         