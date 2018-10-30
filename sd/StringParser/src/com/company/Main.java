package com.company;
import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) {
        Scanner userInput = new Scanner(System.in);

        System.out.print("Language ID: ");
        String languageID = userInput.nextLine();

        System.out.print("Input Text: ");
        String inputText = userInput.nextLine();

        String filteredText = parseString(languageID,inputText);
        System.out.print(filteredText);
    }

    public static String parseString(String languageID, String inputText)
    {
        try
        {
            HashSet<String> blackList = FileAdapter.blackListFromLanguageID(languageID);
            return StringFilter.filter(inputText,blackList);
        }
        catch(IOException e)
        {
            e.printStackTrace();
        }

        return null;
    }
}
