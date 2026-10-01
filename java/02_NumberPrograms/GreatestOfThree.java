import java.util.Scanner;

public class GreatestOfThree {
    public static void main(String[] args) {
        try (var sc = new Scanner(System.in)) {
            System.out.print("Enter a: ");
            var a = sc.nextInt();
            System.out.print("Enter b: ");
            var b = sc.nextInt();
            System.out.print("Enter c: ");
            var c = sc.nextInt();

            var greatest = (a > b) ? (a > c ? a : c) : (b > c ? b : c);
            System.out.println("Greatest: " + greatest);

            if (greatest % 2 == 0) System.out.println(greatest + " is EVEN");
            else                   System.out.println(greatest + " is ODD");
        }
    }
}
