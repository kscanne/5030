package com.company;
import java.text.Normalizer;
import java.util.*;

public class StringFilter {

    public static String filter(String inputString, HashSet<String> blackList)
    {
        inputString = Normalizer.normalize(inputString, Normalizer.Form.NFC);
        boolean firstPass = true;
        Scanner scanner = new Scanner(inputString);
        StringBuilder stringBuilder = new StringBuilder();

        // \s is a Java Pattern that represents all forms of white-space
        scanner.useDelimiter("\\s");

        while(scanner.hasNext())
        {
            String currentWord = scanner.next();
            if (blackList.contains(currentWord.toUpperCase()))
            {
                //Do nothing, word is a stopword
            } else {
                if (!firstPass)
                    stringBuilder.append(" " + currentWord);
                else {
                    stringBuilder.append(currentWord);
                    firstPass = false;
                }
            }
        }

        return stringBuilder.toString();
    }
}
