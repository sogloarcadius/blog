
class Problem2 {
    
    
    public static void main (String[] args) {
        
        long n=4000001;
        long U0 = 1;
        long U1 = 2;
        long UN = 0;
        long sum_fibo_even_values = 2;
        
        while ( UN < n ) {
            UN = U0 + U1;
            if (UN % 2 == 0){
                sum_fibo_even_values = sum_fibo_even_values + UN ;
            }
            U0 = U1;
            U1 = UN;    
        }
        
        System.out.println(sum_fibo_even_values);
        
    }
    
}