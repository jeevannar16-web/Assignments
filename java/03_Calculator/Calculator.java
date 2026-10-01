import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        try (var sc = new Scanner(System.in)) {
            System.out.print("Enter a: ");
            var a = sc.nextDouble();
            System.out.print("Enter b: ");
            var b = sc.nextDouble();

            System.out.println("Add : " + (a + b));
            System.out.println("Sub : " + (a - b));
            System.out.println("Mul : " + (a * b));
            System.out.println("Div : " + (a / b));
        }
    }
}
