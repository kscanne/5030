package com.company;

import com.company.util.Stripper;
import com.company.util.StripperException;

import java.io.IOException;

/**
 * This is an example of Stripper usage
 */
public class Main {

    public static void main(String[] args) {

        try {

            String dataDir = "/home/matteo/SoftwareDev/5030/data";
            String str = "The walking dead";
            String languageCode = "en";

            Stripper s = new Stripper(dataDir);

            String res = s.stripStopwords(languageCode, str);
            System.out.println(res);

        } catch (IOException | StripperException e) {
            e.printStackTrace();
        }

    }

}

