package com.cletus.app;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class QueryProcessor {

    private static String stripStopWords(String query, String lang) {
        Scanner sc = null;
        File file;
        ArrayList<String> list = null;
        try {
            file = new File("../data/" + lang + ".txt");
            sc = new Scanner(file);

            String[] queryArray = query.toLowerCase().split(" ");
            list = new ArrayList<>(Arrays.asList(queryArray));

            while (sc.hasNextLine()) {
                String stopWord = sc.nextLine().toLowerCase();
                list.remove(stopWord);
            }

        } catch (FileNotFoundException e) {
            System.out.println(e.getMessage());
        } finally {
            if (sc != null) {
                sc.close();
            }
        }

        assert list != null;
        return listToSentence(list);
    }
    private static String listToSentence(ArrayList<String> list)
    {
        StringBuilder sentence = new StringBuilder();
        for (Object object : list) {
            sentence.append(object).append(" ");
        }

        return sentence.toString().trim();
    }

    public static void main(String[] args) {
        String query = "When the world is standing still";
        String lang = "en";
        String processedQuery = stripStopWords(query, lang);
        System.out.println(processedQuery);
    }
}