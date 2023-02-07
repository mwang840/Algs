public class highestValList {
    public static int findHighestValue(int [] values){
        if(values.length == 0){
            return 0;
        }
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
    int []numbers2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int []noNumbers = {};
    //Should give me 29
    System.out.println(findHighestValue(numbers));
    //Should give me 10
    System.out.println(findHighestValue(numbers2));
    //Should Return Null
    System.out.println(findHighestValue(noNumbers));
}
}