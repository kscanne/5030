package com.company;
import java.nio.file.Paths;
import java.text.Normalizer;
import java.util.*;
import java.io.*;

public class FileAdapter {

    public static HashSet<String> blackListFromLanguageID(String languageID) throws IOException
    {
        HashSet<String> ids = loadListOfIDs();
        if (ids.contains(languageID))
        {
            File file = Paths.get("src\\data\\"+languageID+".txt").toRealPath().toFile();
            Scanner scanner = new Scanner(file);

            // we just need to use \s as delimiter
            scanner.useDelimiter("\\s");

            HashSet<String> wordSet = new HashSet<>();

            while(scanner.hasNext())
            {
                String temp = scanner.next().toUpperCase();
                temp = Normalizer.normalize(temp, Normalizer.Form.NFC);
                wordSet.add(temp);
            }

            return wordSet;
        } else {
            //Throw error or something to the console
            throw new IllegalArgumentException("Error: Not a valid language code");
        }
    }

    private static HashSet<String> loadListOfIDs() throws IOException
    {
        File file = Paths.get("src\\data\\list.txt").toRealPath().toFile();

        Scanner scanner = new Scanner(file);

        //we just need to use \s as delimiter
        scanner.useDelimiter("\\s");

        HashSet<String> ids = new HashSet<>();

        while(scanner.hasNext())
        {
            ids.add(scanner.next());
        }

        return ids;
    }
}
