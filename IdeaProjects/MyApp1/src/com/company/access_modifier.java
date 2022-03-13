package com.company;

class MyEmployee{
    private int id;
    private String name;

    public void setId(int i){
        this.id = 69;
    }
    public int getId(){
        return id;
    }
}

public class access_modifier {
    public static void main(String[] args) {
        MyEmployee harry = new MyEmployee();
//        harry.id = 89;
//        harry.name = "Something"; //Throws an error due to private access modifier
        harry.setId(47);
        System.out.println(harry.getId());
    }
}
