package com.cletus.app;

import java.io.*;
import java.util.*;

public class QueryProcessor {

    public static String stripStopWords(String lang, String query) {

        ArrayList<String> list = null;
        try (BufferedReader file = new BufferedReader(new FileReader("../data/" + lang + ".txt"))) {
            String stopWord = file.readLine().toLowerCase();
            String[] queryArray = query.toLowerCase().split("\\s+"); //using "\s+" regex for a white space character one or more times
            list = new ArrayList<>(Arrays.asList(queryArray));

            while (stopWord != null) {
                list.remove(stopWord);
                stopWord = file.readLine();
            }

        } catch (IOException e) {
            System.out.println(e.getMessage());
        }

        assert list != null;
        return listToSentence(list);
    }

    private static String listToSentence(ArrayList<String> list) {
        StringBuilder sentence = new StringBuilder();
        for (Object object : list) {
            sentence.append(object).append(" ");
        }

        return sentence.toString().trim();
    }
}