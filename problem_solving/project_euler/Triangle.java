import java.util.LinkedList;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Arrays;

public class Triangle {


    public static void main(String [] args) {

        LinkedList<int []> data = new LinkedList<int[]>();


        //read file
        try {
            BufferedReader bufferedReader = new BufferedReader(new FileReader("p067_triangle.txt"));

            int i=0;
            while (i < 100) {
                i=i+1;
                String [] line = bufferedReader.readLine().split(" ");
                int [] arr = new int [line.length];
                for (int j=0; j<arr.length; j++){
                    arr[j] = Integer.parseInt(line[j]);
                }

                data.add(arr);
            }
        } catch(Exception ex){
            ex.printStackTrace();
        }

        //System.out.println(Arrays.toString(data.get(99)));

        //compute sum_max_path
        while (data.size() > 1) {
            int [] t0 = data.pollLast();
            int [] t1 = data.pollLast();

            int [] tnew = new int[t1.length];

            for (int k=0; k<t1.length; k++){
                tnew[k] = Math.max(t0[k], t0[k+1]) + t1[k];
            }
            data.add(tnew);
        }

        System.out.println(data.get(0)[0]);

    }
}