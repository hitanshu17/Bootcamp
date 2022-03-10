package com.company;

import java.util.Scanner;

public class inputFromUser {
    public static void main(String[] args) {
        System.out.println("Taking input from user");

        //Program to Add 2 nos
//        Scanner sc = new Scanner(System.in);
//        System.out.println("Enter 1st No");
//        int num1 = sc.nextInt();
//        System.out.println("Enter 2nd No");
//        int num2 = sc.nextInt();
//        int num3 = num1 + num2;
//        System.out.println(num3);

        //Checking if entered input is int or not
//        Scanner sc = new Scanner(System.in);
//        boolean b1 = sc.hasNextInt();
//        System.out.println(b1);

        //Printing a string input received from user
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        System.out.println(str);
    }

}
