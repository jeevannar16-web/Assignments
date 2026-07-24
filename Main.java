class Student{
    String name;
    int age;
    Student(String n, int a){
        name=n;
        age=a;
    }
    void display(){
        System.out.println("Name= " + name + " Age = " + age);
    }
}
public class Main
{
public static void main(String[] args) {
    Student s1 = new Student("Arjun" , 20);
    s1.display();
}
}
