//import java.util.Arrays;

public class LearnHub {
   public static void main(String[] args) {
   
   java.util.Scanner inputCollector = new java.util.Scanner(System.in);

   System.out.println("========    LEARN   HUB    ========");

   //ArrayList<String> quizScore() = new ArrayList<>();
 
   System.out.print("Enter Number Of Students Enrolled: ");
   int numbersOfStudent = inputCollector.nextInt();

   System.out.print("Enter Number Of Quiz Taken: ");
   int numbersOfQuiz = inputCollector.nextInt();

   String[] studentName = new String[numbersOfStudent]; //array to hold numbers of students.
 
   //grid holding integer scores. Rows = student, Column = Quizzes
   int[][] quizScores = new int[numbersOfStudent][numbersOfQuiz];

   for(int students = 1; students < numbersOfStudent + 1; students++) {
       System.out.println();
       System.out.println("=====    Student " + students + " =====");

       for(int quiz = 1; quiz < numbersOfQuiz + 1; quiz++) {
           System.out.print("Score For Quiz " + quiz + ": ");
	   int quizInput = inputCollector.nextInt();
       }
   }

   

   }//main
}//class
