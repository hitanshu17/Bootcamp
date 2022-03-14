package com.company;

import java.util.Scanner;

public class task {

    static int sum(int a, int b){
        return a+b;
    }

    public static void main(String[] args) {

        float number_1, number_2;
        System.out.println("Enter 1st Number");

        Scanner scan = new Scanner(System.in);
        number_1 = scan.nextFloat();

        System.out.println("Enter 2nd Number");
        number_2 = scan.nextFloat();
        System.out.print("Numbers entered: ");
        System.out.print(number_1);
        System.out.print(" & ");
        System.out.println(number_2);
        String prompt = "Enter 0 for addition, 1 for subtraction, 2 for multiplication and 3 for division";
        System.out.println(prompt);
        int input = scan.nextInt();
        switch (input){
            case 0:
                System.out.println("On Adding");
                System.out.print("Result= ");
                System.out.println(number_1 + number_2);
                break;

            case 1:
                System.out.println("On Subtracting");
                System.out.print("Result= ");
                System.out.println(number_1 - number_2);
                break;

            case 2:
                System.out.println("On Multiplying");
                System.out.print("Result= ");
                System.out.println(number_1 * number_2);
                break;

            case 3:
                System.out.println("On Dividing");
                System.out.print("Result= ");
                System.out.println(number_1 / number_2);
                break;

            default:
                System.out.println("Invalid input");

        }

    }
}

