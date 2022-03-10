package com.company;

import java.util.Scanner;

public class Program1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Marks of Sub 1");
        float sub1 = sc.nextInt();
        System.out.println("Enter Marks of Sub 2");
        float sub2 = sc.nextInt();
        System.out.println("Enter Marks of Sub 3");
        float sub3 = sc.nextInt();
        float percentage = ( (sub1 + sub2 + sub3)/300 ) * 100;
        System.out.println("Percentage " + percentage);
    }
}
