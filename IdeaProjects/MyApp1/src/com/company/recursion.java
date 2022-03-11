package com.company;

public class recursion {

    static boolean fun2(int n){
        if(n>0){
            fun2(n-1);
            System.out.println(n);
        }
        return false;
    }
    public static void main(String[] args) {
        int n = 10;
        System.out.println(fun2(n));
    }
}
