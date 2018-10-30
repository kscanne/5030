package com.company;

import com.company.util.Stripper;
import com.company.util.StripperException;

import java.io.IOException;

public class Main {

    public static void main(String[] args) {
        // write your code here
        try {
            String str = "The walking dead";
            Stripper s = new Stripper("//home//matteo//SoftwareDev//5030//data");
            System.out.println(s.stripStopwords("en", str));
        } catch (IOException | StripperException e) {
            e.printStackTrace();
        }

    }

}

