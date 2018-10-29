package com.cletus.app;

import java.io.*;
import java.util.*;

public class QueryProcessor {

    private static String stripStopWords(String lang, String query) {
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

    private static String listToSentence(ArrayList<String> list) {
        StringBuilder sentence = new StringBuilder();
        for (Object object : list) {
            sentence.append(object).append(" ");
        }

        return sentence.toString().trim();
    }

    public static void test(String fileName) {
        StringTokenizer token;
        try (BufferedReader file = new BufferedReader(new FileReader(fileName))) {
            String line = file.readLine();

            while (line != null) {
                token = new StringTokenizer(line, "\t"); //.tsv files are delimited by tabs, hence the "\t"
                List<String> dataArray = new ArrayList<>();
                while (token.hasMoreElements()) {
                    dataArray.add(token.nextElement().toString());
                }

                String processedQuery = stripStopWords(dataArray.get(0), dataArray.get(1));
                System.out.println(processedQuery);

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