import java.util.Scanner;

public class InputDemo {
    public static void main(String[] args) {
        try (var sc = new Scanner(System.in)) {
            System.out.print("Enter your name: ");
            var name = sc.nextLine();

            System.out.print("Enter your age: ");
            var age = sc.nextInt();

            System.out.println("Hello " + name + ", you are " + age + " years old!");
        }
    }
}
