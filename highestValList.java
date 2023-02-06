public class highestValList {
    public static int findHighestValue(int [] values){
        int MAX = values[0];
        for(int i = 1; i < values.length; i++){
            if(values[i] > MAX){
                MAX = values[i];
            }
        }
        return MAX;
    }
public static void main(String[] args) {
    int []numbers = {5, 1, 2, 15, 29, 25, 26};
    System.out.println(findHighestValue(numbers));
}
}