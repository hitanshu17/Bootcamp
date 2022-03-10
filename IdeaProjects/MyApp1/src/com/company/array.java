package com.company;

public class array {
    public static void main(String[] args) {

        //ways to create array in java
//        1-> declaration and memory allocation
//        eg:-
//        int [] marks = new int[5];
//        marks[0] = 100;
//        marks[1] = 90;
//        marks[2] = 80;
//        marks[3] = 70;
//        marks[4] = 60;
//        System.out.println(marks[2]);
//
//        2-> declaration then memory allocation
//        eg:-
//        int [] marks;
//        marks = new int[5];
//        marks[0] = 100;
//        marks[1] = 90;
//        marks[2] = 80;
//        marks[3] = 70;
//        marks[4] = 60;
//        System.out.println(marks[2]);
//
//        3-> Declaration, memory allocation and initiation together
//         eg:-
//         int [] marks = {100,90,80,70,60};
//         System.out.println(marks[2]);
//         System.out.println(marks.length);

         String [] students = {"Harry","Rohan","Shubham"};

         //Displaying the array (naive way)
//        System.out.println(students[2]);
//        System.out.println(students.length);

        //Displaying the array (for loop)
//        for (int i=0; i<students.length;i++){
//            System.out.println(students[i]);
//        }

        //reverse order
//        for (int i=students.length -1; i>=0;i--){
//            System.out.println(students[i]);
//        }

        //Displaying the array (for each)
        for (String element:students){
            System.out.println(element);
        }

    }
}
