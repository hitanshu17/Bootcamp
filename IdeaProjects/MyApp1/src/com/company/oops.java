package com.company;

class Employee{
    int id;
    String name;
    public void printDetails(){
        System.out.println("My id =" + id);
        System.out.println("And my name is" + name);
    }
}

public class oops {
    public static void main(String[] args) {
        //Instantiating a new Employee object
        Employee harry = new Employee();
        //Setting Properties
        harry.id = 69;
        harry.name = "Harry";
        //Printing the attributes
//        System.out.println(harry.id);
//        System.out.println(harry.name);
        harry.printDetails();
    }
}
