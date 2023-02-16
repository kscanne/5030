package com.firstspringproject.Controllers;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.util.*;

public class ToLowerCase {
    
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
    public static void main(String args[]) throws UnsupportedEncodingException
    {
        // words to be converted to lowerCase
        String words[] = {"HELLO", "WORLD", "cAmEl", "---OK", "tAcht", "tACHT", "TACHT", "nAthair", "nATHAIR",
        "NATHAIR", "tOthair", "tETHAIR", "tITHAIR", "nÓg", "nÕg","对不起","ごめんなさい", "KASIM", "KASIM", "ΠΌΛΗΣ", "官话", "ภาษาไทย", "ΠΌΛΗΣ", "ΠΌΛΗΣΠΌΛΗΣ"};
        
        // words in their respective languages 
        String lang[] = {"en", "en-US", "en-IE", "en-Latn", "ga", "ga", "ga", "ga", "ga",
         "ga", "ga", "ga", "ga", "ga-IE", "ga-IE", "zh", "ja", "az", "en", "el", "zh-Hans", "th", "el-GR", "el-GR"};

        String langWithNoLowerCase[] = {"zh", "ja", "th"};
        
        PrintWriter printWriter = null;
        try {
            printWriter = new PrintWriter("D:\\SLU\\Spring 23\\PSD\\result.txt", "UTF-8");
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        ToLowerCase object = new ToLowerCase();
      for(int i=0;i<words.length;i++)
      {
        String result = object.wordToLowerCase(words[i],lang[i],langWithNoLowerCase);
        printWriter.println(words[i]+ " " + lang[i] +" "+result);
      }
      
      printWriter.close();
     
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
