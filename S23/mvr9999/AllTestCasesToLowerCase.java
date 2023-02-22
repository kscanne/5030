package com.firstspringproject.Controllers;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.util.*;

public class AllTestCasesToLowerCase {
    
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
        AllTestCasesToLowerCase object = new AllTestCasesToLowerCase();
      for(int i=0;i<words.length;i++)
      {
        String result = object.wordToLowerCase(words[i],lang[i],langWithNoLowerCase);
        printWriter.println(words[i]+ " " + lang[i] +" "+result);
      }
      printWriter.close();
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
