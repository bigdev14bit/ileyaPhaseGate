import java.util.Arrays;

public class MbitTestApp {
   public static void main(String[] args) {
   
   java.util.Scanner inputCollector = new java.util.Scanner(System.in);

   String menu = ("""
=================================================================
WELCOME TO GBEDA PETROLEUM STATION!
=================================================================
-----------------------------------------------------------------
Available petroleum
   1. Buy Petroleum
   2. Show Transaction History
-----------------------------------------------------------------
		   """);

   String availablePetroleum = ("""
=================================================================		   
1. PETROL == >   650/L
2. DIESEL == >   720/L
3. KEROSENE == >   550/L
4. GAS == >   480/L
=================================================================
		   """);

while(true) {
    System.out.println(menu);
    System.out.println();

    System.out.print("Enter An Option: ");
    String userInput = inputCollector.nextLine();

    if(userInput == "quit") {
        System.out.println("Exit Successfully!!!");
	break;
    } // if condition to terminate while true
    else {
        return;
    } // else do this.

} //while true????

   } // method
} // class
