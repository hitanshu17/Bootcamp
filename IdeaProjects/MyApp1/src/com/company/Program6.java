package com.company;

public class Program6 {
    public static void main(String[] args) {

        // Program 1
//        float [] marks = {10.9f,23.2f,98.2f,73.4f};
//        float sum = 0;
//        for (float element:marks){
//            sum += element;
//        }
//        System.out.println("Total " + sum);

        //Program 2
//        float [] marks = {10.9f,23.2f,98.2f,73.4f};
//        float num = 123.2f;
//        boolean isInArray = false;
//        for (float element:marks){
//            if (num == element){
//                isInArray = true;
//                break;
//            }
//        }
//        if (isInArray){
//            System.out.println("True");
//        }
//        else {
//            System.out.println("False");
//        }

        //Program 3
//        int [][] mat1 = { {1,2,3} , {4,5,6} };
//        int [][] mat2 = { {2,6,13}, {3,7,1} };
//        int [][] result = { {0,0,0}, {0,0,0} };
//
//        for (int i=0;i<mat1.length;i++){
//            for (int j=0;j<mat1[i].length;j++) {
//                //System.out.format("Setting value for i = %d and j = %d \n",i,j);
//                System.out.print(result[i][j] + " ");
//                result[i][j] = mat1[i][j] + mat2[i][j];
//            }
//            System.out.println("");
//        }

        // Program 4 Reversing an Array

//        int [] arr = {1,2,3,4,5,6};
//        int l = arr.length;
//        int n = Math.floorDiv(l, 2);
//        int temp;
//
//        for (int i=0;i<n;i++){
//            //Swap a[i] and a[l-i-1]
//            temp = arr[i];
//            arr[i] = arr[l-i-1];
//            arr[l-i-1] = temp;
//        }
//        for (int element: arr){
//            System.out.print(element + " ");
//        }

        // Practise 5 max no

//        int [] arr2 = {21,27,13,34,500,65};
//        int max = 0;
//        for (int element:arr2){
//            if (element > max){
//                max = element;
//            }
//        }
//        System.out.println(max);

        // Practise 6 min no

//        int [] arr2 = {21,27,13,34,500,65};
//        int min = Integer.MAX_VALUE;
//        for (int element:arr2){
//            if (element < min){
//                min = element;
//            }
//        }
//        System.out.println(min);

        //Practise 7 given array sorted or not

        int [] arr3 = {21,27,13,34,500,65};
        boolean isSorted = true;
        for(int i=0; i<arr3.length-1;i++){
            if(arr3[i] > arr3[i+1]){
                isSorted = false;
                break;
            }
        }
        if(isSorted){
            System.out.println("Sorted");
        } else {
            System.out.println("Not sorted");
        }

    }
}
