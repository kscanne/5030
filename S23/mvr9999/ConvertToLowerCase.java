package com.firstspringproject.Controllers;

import java.util.*;

public class ConvertToLowerCase {

    String turkish_lang = "tr";
    String azerbaijani_lang = "az";
    String irish_lang = "ga";
    String latin_Dotless_I = "\u0131";

    String upper_Case_I = "I";
    char lowerCase_t = 't';
    char lowerCase_n = 'n';

    // Ascii values of vowels
    int upperCase_A = 65;
    int upperCase_E = 69;
    int upperCase_I = 73;
    int upperCase_O = 79;
    int upperCase_U = 85;
   
    int upperCase_Irish_A = 193;
    int upperCase_Irish_E = 201;
    int upperCase_Irish_I = 205;
    int upperCase_Irish_O = 211;
    int upperCase_Irish_U = 218;

    
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
        if(isLanguage_with_no_lowerCase(langWithNoLowerCase, language))
            return word;
        
        Locale locale1 = Locale.forLanguageTag(language);
        
        String lower1 = word.toLowerCase(locale1);
        if(language.startsWith(turkish_lang) || language.startsWith(azerbaijani_lang))
        {
            if(word.contains(upper_Case_I))
            {
                word.replaceAll(upper_Case_I,latin_Dotless_I );
                lower1 = word.toLowerCase(locale1);
            }
        }
        else if(language.startsWith(irish_lang))
        {
            if((word.charAt(0) == lowerCase_n || word.charAt(0) == lowerCase_t) &&
                (word.charAt(1) == upperCase_A || word.charAt(1) == upperCase_E ||
                word.charAt(1) == upperCase_I || word.charAt(1) == upperCase_O||  
                word.charAt(1) == upperCase_U || word.charAt(1) == upperCase_Irish_A ||
                word.charAt(1) == upperCase_Irish_E || word.charAt(1) == upperCase_Irish_I ||
                word.charAt(1) == upperCase_Irish_O || word.charAt(1) == upperCase_Irish_U))
            {
                lower1 = lower1.substring(0,1) +"-" + lower1.substring(1);
            }
        }
      
            return lower1;
    }

    boolean isLanguage_with_no_lowerCase(String []langWithNoLowerCase,String language)
    {
        for(String noLowerCaselang:langWithNoLowerCase)
        {
            if(language.startsWith(noLowerCaselang))
                return true;
        }
        return false;
    }
    
}
