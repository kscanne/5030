package com.company;

import com.company.util.Stripper;
import com.company.util.StripperException;

import java.io.IOException;

public class Main {

    public static void main(String[] args) {
        // write your code here
        try {
            String str = "a la mode";
            Stripper s = new Stripper("//home//matteo//SoftwareDev//5030//data");
            System.out.println(s.stripStopwords("fr", str));
        } catch (IOException | StripperException e) {
            e.printStackTrace();
        }

    }

}

