// import java.util.Scanner;


// public class practice {
//     public static void main(String[] args) {
//         System.out.println("Hello, World!");

//         Scanner p = new Scanner(System.in); 
//         int n = p.nextInt();
//         System.out.println("You entered: " + n);

//         System.out.println("Enter a string:");
//         Scanner s = new Scanner(System.in); 
//         String ss = s.nextLine();
//         System.out.println("You entered: " + ss);

//     }
// }


class Player { 
static int count = 0; 
Player() { 
count++; 
} 
} 
class practice { 
public static void main(String[] args) { 
new Player(); 
new Player(); 
new Player(); 
System.out.println("Players created: " + Player.count); 
} 
} 
