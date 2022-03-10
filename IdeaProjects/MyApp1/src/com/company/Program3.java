package com.company;

public class Program3 {
    public static void main(String[] args) {

        //Problem 1
        String name = "Hitanshu Vig";
        name = name.toLowerCase();
        System.out.println(name);

        //Problem 2
        String test = "This is a problem";
        test = test.replace(" ","_");
        System.out.println(test);

        //Problem 3

        String test2 = "Dear <|name|> , Thanks a lot";
        test2 = test2.replace("<|name|>","Hitanshu");
        System.out.println(test2);

        //Problem 4

        String letter = "This string contains     double and triple spaces";
        System.out.println(letter.indexOf("   "));

        //Problem 5

        String letter2 = "Dear Harry, \n this \t java course is nice";
        System.out.println(letter2);
    }
}
