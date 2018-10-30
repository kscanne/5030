package com.company;
import java.nio.file.Paths;
import java.util.*;
import java.io.*;

public class FileAdapter {

    public static HashSet<String> blackListFromLanguageID(String languageID) throws IOException
    {
        HashSet<String> ids = loadListOfIDs();
        if (ids.contains(languageID))
        {
            File file = Paths.get("data\\"+languageID+".txt").toFile();
            Scanner scanner = new Scanner(file);

            // we just need to use \s as delimiter
            scanner.useDelimiter("\\s");

            HashSet<String> wordSet = new HashSet<>();

            while(scanner.hasNext())
            {
                wordSet.add(scanner.next().toUpperCase());
            }

            return wordSet;
        } else {
            //Throw error or something to the console
            return new HashSet<String>();
        }
    }

    private static HashSet<String> loadListOfIDs() throws IOException
    {
        File file = Paths.get("data\\list.txt").toFile();

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
