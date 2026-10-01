import java.util.Scanner;

public class OddEven {
    public static void main(String[] args) {
        try (var sc = new Scanner(System.in)) {
            System.out.print("Enter a number: ");
            var num = sc.nextInt();

            if (num % 2 == 0) System.out.println(num + " is EVEN");
            else              System.out.println(num + " is ODD");
        }
    }
}
