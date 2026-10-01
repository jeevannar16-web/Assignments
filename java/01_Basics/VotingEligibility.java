import java.util.Scanner;

public class VotingEligibility {
    public static void main(String[] args) {
        try (var sc = new Scanner(System.in)) {
            System.out.print("Enter age: ");
            var age = sc.nextInt();

            System.out.println("Ternary : " + (age >= 18 ? "Can vote" : "Cannot vote"));

            if (age >= 18) System.out.println("If-Else : Can vote");
            else           System.out.println("If-Else : Cannot vote");
        }
    }
}
