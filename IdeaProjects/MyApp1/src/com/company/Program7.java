package com.company;

public class Program7 {

    //Problem 1
//    static void multiplication(int n){
//        for (int i=1;i<=10;i++) {
//            System.out.format("%d X %d = %d\n", n, i, n * i);
//        }
//    }

    //Problem 2
//    static void pattern(int n){
//        for (int i=0;i<n;i++){
//            for (int j=0;j<i;j++){
//                System.out.print("x");
//            }
//            System.out.print("\n");
//        }
//    }

    //Problem 3
    static int sumRec (int n){
        if (n==1){
            return 1;
        }
        return n + sumRec(n-1);

    }

    public static void main(String[] args) {
//        multiplication(7);
//        pattern(5);
        System.out.println(sumRec(10));
    }
}
