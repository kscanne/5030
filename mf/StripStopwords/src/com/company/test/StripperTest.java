package com.company.test;

import com.company.util.Stripper;
import com.company.util.StripperException;
import junit.framework.TestCase;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class StripperTest extends TestCase {

    private Stripper stripper;
    private List<String> languageCodes;
    private List<String> strings;
    private List<String> expecteds;
    private int numTests;


    public void setUp() throws Exception {

        super.setUp();
        stripper = new Stripper("//home//matteo//SoftwareDev//5030//data");
        languageCodes = new ArrayList<>();
        strings = new ArrayList<>();
        expecteds = new ArrayList<>();

        File file = new File("//home//matteo//SoftwareDev//5030//tests//cases.tsv");

        BufferedReader br = new BufferedReader(new FileReader(file));

        String line;
        while ((line = br.readLine()) != null){


            StringTokenizer st = new StringTokenizer(line, "\t");

            if(st.hasMoreTokens()) {
                languageCodes.add(st.nextToken());
                if(st.hasMoreTokens()) {
                    strings.add(st.nextToken());
                    if(st.hasMoreTokens()) {
                        expecteds.add(st.nextToken());
                    } else {
                        expecteds.add("");
                    }
                } else {
                    strings.add("");
                    expecteds.add("");
                }
            } else {
                languageCodes.add("");
                strings.add("");
                expecteds.add("");
            }



        }

        numTests = languageCodes.size();

    }

    public void testStripStopwords() {

        try {

            for(int i = 0; i < numTests; i++) {

                String languageCode = languageCodes.get(i);
                String string = strings.get(i);
                String expected = expecteds.get(i);

                String actual = stripper.stripStopwords(languageCode, string);

                assertEquals("Test " + (i+1) + " has failed", expected, actual);

            }

        } catch (IOException | StripperException e) {
            e.printStackTrace();
        }

    }
}