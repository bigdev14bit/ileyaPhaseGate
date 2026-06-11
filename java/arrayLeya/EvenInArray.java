import java.util.ArrayList;

public class EvenInArray {
   public static void main(String[] args) {
   
   int[] myArray = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

   ArrayList<Integer> addEven = new ArrayList<>();
   ArrayList<Integer> oddNumber = new ArrayList<>();

   for(int numbers : myArray) {
      if(numbers % 2 == 0) {
         addEven.add(numbers);
      } else {
         oddNumber.add(numbers);
      }
   }

   System.out.println("Even number: " + addEven);
   System.out.println("Odd number: " + oddNumber);
   System.out.println("Both : " + addEven + " " + oddNumber);
   }
}
