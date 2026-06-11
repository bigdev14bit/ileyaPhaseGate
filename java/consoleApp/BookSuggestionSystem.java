import java.util.Random;

public class BookSuggestionSystem {
   public static void main(String[] args) {
   
   java.util.Scanner inputCollector = new java.util.Scanner(System.in);

   System.out.print("BOOK recommending SYSTEM");

   String books = {[
       [
      {"title": "Clean Code", "author": "Robert C. Martins", "genre": "Programming", "page": ""},
      {"title": "Java How To Programmer", "author": "Paul Dietel", "genre": "Programming", "page": 1286},
      {"title": "A Woman Of Substance", "author": "Barbara Taylor Bradford", "genre": "Novel", "page": ""},
      {"title": "The Psychology of Persuasion", "author": "Robert B. Cialdini", "genre": "Socials", "page": ""},
      {"title": "Dune", "author": "Frank Herbert", "genre": "Sci-fi", "page": ""},
      {"title": "The alchemist", "author": "", "genre": "Fiction", "page": ""},
      {"title": "The name of the wind", "author": "Patrick Rothfuss", "genre": "Fantasy", "page": ""}
        ]
   ]}

   String menu = ("

===========================================================================================
          WELCOME TO BOOK RECOMMENDER
===========================================================================================

1. Get Random Recommendation
2. Filter By Genre
3. Add Book
4. Remove Book
5. View my stats
6. Mark All As Read
7. Show all books
8. Exit
""");

   System.out.print(menu);

   while(true) {
       System.out.print("Enter Option: ")
       String userInput = inputCollector.nextLine();

       if(userInput == 5) {
           System.out.println("EXIT SUCCESSFULLY!!")
	   break;
       }

       else if(userInput == 1) {
           String recommendedBook = 
       } 
   }//while true
   }
}
