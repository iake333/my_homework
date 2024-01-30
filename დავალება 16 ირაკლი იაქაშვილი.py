#1.	შექმენი წრის კლასი, რომელსაც ექნება მეთოდები საკუთარი პერიმეტრისა და ფართობის გამოსათვლელად.
import math

class Circle:
    pi_value = math.pi

    @staticmethod
    def circle_area(r):
        area = Circle.pi_value * r**2
        return area

    @staticmethod
    def circle_perimeter(r):
        perimeter = 2 * Circle.pi_value * r
        return perimeter


radius = float(input("Enter the radius: "))
area_result = Circle.circle_area(radius)
perimeter_result = Circle.circle_perimeter(radius)

print(f"Area: {area_result}")
print(f"Perimeter: {perimeter_result}")
#2.	შექმენი კალკულატორის კლასი, საბაზისო არითმეტიკული ოპერაციების მეთოდებით.
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"


calculator = Calculator()

result_add = calculator.add(5, 3)
print(f"Addition: {result_add}")

result_subtract = calculator.subtract(10, 4)
print(f"Subtraction: {result_subtract}")

result_multiply = calculator.multiply(3, 7)
print(f"Multiplication: {result_multiply}")

result_divide = calculator.divide(8, 2)
print(f"Division: {result_divide}")
