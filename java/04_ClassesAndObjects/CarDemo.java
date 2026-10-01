public class CarDemo {
    public static void main(String[] args) {
        var myCar = new Car();
        myCar.brand = "Toyota";
        myCar.color = "Red";
        myCar.speed = 0;

        var yourCar = new Car();
        yourCar.brand = "Honda";
        yourCar.color = "Blue";
        yourCar.speed = 20;

        myCar.show();
        myCar.accelerate();
        myCar.accelerate();

        yourCar.show();
        yourCar.accelerate();
    }
}

class Car {
    String brand;
    String color;
    int speed;

    void accelerate() {
        speed += 10;
        System.out.println(color + " " + brand + " at " + speed + " km/h");
    }

    void show() {
        System.out.println(brand + " " + color + " (" + speed + " km/h)");
    }
}
