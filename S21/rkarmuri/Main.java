//Main Program to convert to lowercase
package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner myWord = new Scanner(System.in);//Input word
        String wordSample;
        Scanner myLang = new Scanner(System.in);//Input language tag
        String language;
        System.out.println("Enter a word to convert to lower case:");
        wordSample = myWord.nextLine();//Move to next line after entering the word
        System.out.println("Enter a language tag:");
        language = myLang.nextLine();//Move to next line after entering the language
        ConvertToLowerCase convertToLowerCase = new ConvertToLowerCase();
        convertToLowerCase.convert(wordSample, language);//Calling the method to execute
    }
}
