import java.util.Scanner;

public class PositiveNegativeZero {
    public static void main(String[] args) {
        try (var sc = new Scanner(System.in)) {
            System.out.print("Enter a number: ");
            var num = sc.nextInt();

            if (num > 0)      System.out.println(num + " is POSITIVE");
            else if (num < 0) System.out.println(num + " is NEGATIVE");
            else              System.out.println(num + " is ZERO");
        }
    }
}
