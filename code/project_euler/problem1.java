
Class Problem1 {
    
    private ArrayList multiples_of_3_or_5;
    private sum_multiples_of_3_or_5;
    
    public void static main (args []) {
        
        multiples_of_3_or_5 = new ArrayList();
        sum_multiples_of_3_or_5 = 0;
        
        for (int number=0; number < 10; number++){
            
            if (isMultiple3or5(number) == true) {
                
                multiples_of_3_or_5.add(number);
                sum_multiples_of_3_or_5+=number;
            }
  
        }
        
        system.out.println(multiples_of_3_or_5.toString());
        system.out.println(sum_multiples_of_3_or_5);
  
    }
    
    
    Bool isMultiple3or5(number) {

        if ((number % 3) == 0 || (number % 5) == 0)){ 
            return true
        } else 

            return false
    }
}
    
    
    
}