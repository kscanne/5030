package com.firstspringproject.Controllers;

import java.util.*;

public class ConvertToLowerCase {

    String turkishLang = "tr";
    String azerbaijaniLang = "az";
    String irishLang = "ga";
    String latinDotlessI = "\u0131";

    String upperCaseI = "I";
    char lowerCaseT = 't';
    char lowerCaseN = 'n';

    // Ascii values of vowels
    int upperCaseA = 65;
    int upperCaseE = 69;
    int upperCaseIInt = 73;
    int upperCaseO = 79;
    int upperCaseU = 85;
   
    int upperCaseIrishA = 193;
    int upperCaseIrishE = 201;
    int upperCaseIrishI = 205;
    int upperCaseIrishO = 211;
    int upperCaseIrishU = 218;

    int vowels[]={upperCaseA,upperCaseE,upperCaseIInt,upperCaseO,upperCaseU,upperCaseIrishA,upperCaseIrishE,upperCaseIrishI,upperCaseIrishO,upperCaseIrishU};
    
    public static void main(String args[])    {
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter the word to be converted to lower case: ");
    String word = sc.nextLine();
    System.out.println("Enter the language of the word to be converted to lower case: ");
    String language = sc.nextLine();
    String langWithNoLowerCase[] = {"zh", "ja", "th"};

    ConvertToLowerCase object = new ConvertToLowerCase();
    String result = object.wordToLowerCase(word,language,langWithNoLowerCase);
    System.out.println("Result : "+result);
    }
    public String wordToLowerCase(String word,String language, String[] langWithNoLowerCase)
    {
        if(isLanguageWithNoLowerCase(langWithNoLowerCase, language))
            return word;
        
        Locale locale1 = Locale.forLanguageTag(language);
        
        String lower1 = word.toLowerCase(locale1);
        if(language.startsWith(turkishLang) || language.startsWith(azerbaijaniLang))
        {
            if(word.contains(upperCaseI))
            {
                word.replaceAll(upperCaseI,latinDotlessI );
                lower1 = word.toLowerCase(locale1);
            }
        }
        else if(language.startsWith(irishLang))
        {
            if((word.charAt(0) == lowerCaseN || word.charAt(0) == lowerCaseT))
            {

            for(Integer vowel:vowels)
            {
                if(word.charAt(1) == vowel)
                {
                lower1 = lower1.substring(0,1) +"-" + lower1.substring(1);
                break;
                }

            } }
        }
      
            return lower1;
    }

    boolean isLanguageWithNoLowerCase(String []langWithNoLowerCase,String language)
    {
        for(String noLowerCaselang:langWithNoLowerCase)
        {
            if(language.startsWith(noLowerCaselang))
                return true;
        }
        return false;
    }
    
}
