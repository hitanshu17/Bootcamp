package com.company;
import java.util.Scanner;

public class conditons {
    public static void main(String[] args) {
        int age;
        System.out.println("Enter Age");
        Scanner sc = new Scanner(System.in);
        age = sc.nextInt();

        //Problem 1
//        if (age<18){
//            System.out.println("bhai kya kar raha hai tu");
//        }
//        else if (age < 17){
//            System.out.println("Almost there");
//        }
//        else {
//            System.out.println("Waah bete moj kardi");
//        }

        //Problem 2

        switch (age){
            case 18:
                System.out.println("College");
                break;
            case 23:
                System.out.println("Job");
                break;
            case 60:
                System.out.println("Retired");
                break;
            default:
                System.out.println("Ye bhi sahi hai");
        }
    }
}
