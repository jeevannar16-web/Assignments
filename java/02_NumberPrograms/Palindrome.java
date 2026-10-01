import java.util.Scanner;

public class Palindrome {
    public static void main(String[] args) {
        try (var sc = new Scanner(System.in)) {
            System.out.print("Enter a number: ");
            var num = sc.nextInt();

            var original = num;
            var reversed = 0;

            while (num > 0) {
                reversed = reversed * 10 + num % 10;
                num /= 10;
            }

            if (original == reversed)
                System.out.println(original + " is a PALINDROME");
            else
                System.out.println(original + " is NOT a palindrome");
        }
    }
}
