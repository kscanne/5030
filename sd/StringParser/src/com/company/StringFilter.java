package com.company;
import java.util.*;

public class StringFilter {

    public static String filter(String inputText, HashSet<String> blackList)
    {
        Scanner scanner = new Scanner(inputText);
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
                stringBuilder.append(currentWord);
                if (scanner.hasNext())
                    stringBuilder.append(" ");
            }
        }

        return stringBuilder.toString();
    }
}
