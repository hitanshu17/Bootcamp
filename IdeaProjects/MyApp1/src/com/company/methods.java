package com.company;

import java.util.Arrays;

public class methods {
    static void tellJoke(){
        System.out.println("Hello World");
    }

    static void change(int [] arr){
        arr[0] =98;
    }

    public static void main(String[] args) {
        //tellJoke();

        //Changing the array value
        int [] marks = {52,43,88,96,69};
        change(marks);
        System.out.println(Arrays.toString(marks));

    }
}
