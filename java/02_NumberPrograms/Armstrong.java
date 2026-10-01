import java.util.Scanner;

public class Armstrong {
    public static void main(String[] args) {
        try (var sc = new Scanner(System.in)) {
            System.out.print("Enter a number: ");
            var num = sc.nextInt();

            var original = num;
            var sum = 0;

            while (num > 0) {
                var digit = num % 10;
                sum += digit * digit * digit;
                num /= 10;
            }

            if (original == sum)
                System.out.println(original + " is an ARMSTRONG number");
            else
                System.out.println(original + " is NOT an Armstrong number");
        }
    }
}
