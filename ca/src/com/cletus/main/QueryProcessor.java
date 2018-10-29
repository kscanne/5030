package com.cletus.main;

import java.io.*;
import java.util.*;

public class QueryProcessor {

    private static String stripStopWords(String lang, String query) {

        ArrayList<String> list = null;
        try (BufferedReader file = new BufferedReader(new FileReader("../data/" + lang + ".txt"))) {
            String stopWord = file.readLine().toLowerCase();
            String[] queryArray = query.toLowerCase().split("\\s+"); //using "\s+" regex for a white space character one or more times
            list = new ArrayList<>(Arrays.asList(queryArray));

            while (stopWord!=null) {
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

    private static void test(String fileName) {
        try (BufferedReader file = new BufferedReader(new FileReader(fileName))) {
            String line = file.readLine();

            int lineCount = 0;
            while (line != null) {
                lineCount++;
                String[] token = line.split("\t"); //.tsv files are delimited by tabs, hence the "\t" regex
                List<String> dataArray = Arrays.asList(token);
                String processedQuery = stripStopWords(dataArray.get(0), dataArray.get(1));
                if(!processedQuery.equals(dataArray.get(2)))
                    System.out.println("Test on line "+lineCount+" failed; expected \""+dataArray.get(1)+"\""+" found "+" \""+processedQuery+"\"");
                    System.out.println("Test on line "+lineCount+" failed; expected \""+dataArray.get(1)+"\""+" found "+" \""+processedQuery+"\"");

                line = file.readLine();
            }
            file.close();
            System.out.println();

        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }

    public static void main(String[] args) {
        test("../tests/" + "cases.tsv");
    }
}