public class StudentDemo {
    public static void main(String[] args) {
        var s1 = new Student();
        s1.name = "Alice";
        s1.age = 15;
        s1.grade = "10th";

        var s2 = new Student();
        s2.name = "Bob";
        s2.age = 16;
        s2.grade = "11th";

        s1.display();
        s2.display();
    }
}

class Student {
    String name;
    int age;
    String grade;

    void display() {
        System.out.println(name + " | " + age + " | " + grade);
    }
}
