//Method to convert given string to lowercase
package com.company;

import java.util.Locale;//Package to accept multiple languages

public class ConvertToLowerCase {
    public String convert(String wordSample, String language) {
        System.out.println("Input word: " + wordSample);
        System.out.println("Input language tag: " + language);
        String wordLowerCase = wordSample.toLowerCase();//Conversion in English
        String trazString = wordSample.toLowerCase(Locale.forLanguageTag("az"));//Conversion in Turkish and Azerbaijani
        String russString = wordSample.toLowerCase(Locale.forLanguageTag("ru-Latn"));//Conversion in Russian
        String hungarianString = wordSample.toLowerCase(Locale.forLanguageTag("hu"));//Conversion in Hungarian
        //Conversion cases for Greek
        String greekString = wordLowerCase.replace('Σ', 'σ').replace('Ε', 'ε').
                replace('Α', 'α').replace('Β', 'β').
                replace('Γ', 'γ').replace('Π', 'π').
                replace('Ό', 'ό').replace('Λ', 'λ').
                replace('Η', 'η').replace('Δ', 'δ').
                replace('Ζ', 'ζ').replace('Θ', 'θ').
                replace('Μ', 'μ').replace('Ν', 'ν').
                replace('Ξ', 'ξ').replace('Ρ', 'ρ').
                replace('Ω', 'ω').replace('Ψ', 'ψ').
                replace('Χ', 'χ').replace('Φ', 'φ').
                replace('Υ', 'υ').replace('Τ', 'τ');
        String outputString;//Variable that is used to return the desired lowercase to test code method
        switch (language) {
            //This case is to convert English, English(US), English(Ireland), English(Latin) and Spanish words
            case "en":
            case "en-US":
            case "en-IE":
            case "en-Latn":
            case "es":
                System.out.println("String after converting to lower case: " + wordLowerCase);
                outputString = wordLowerCase;
                break;
            //This case is to convert Turkish and Azerbaijan words
            case "tr":
            case "az":
                System.out.println("String after converting to lower case: " + trazString);
                outputString = trazString;
                break;
            //This case is to convert all Greek words
            case "el":
                if (wordSample.endsWith("Σ")) {
                    //Replacing Word ending with Sigma condition
                    String newString = wordLowerCase.replace('Σ', 'ς');
                    System.out.println("String after converting to lower case: " + newString);
                    outputString = newString;
                } else {
                    //Print and return the output lowercase in greek
                    System.out.println("String after converting to lower case:" + greekString);
                    outputString = greekString;
                }
                break;
            //This case is to convert Russian words
            case "ru-Latn":
                System.out.println("String after converting to lower case: " + russString);
                outputString = russString;
                break;
            //This case is to convert Hungarian words
            case "hu":
                System.out.println("String after converting to lower case: " + hungarianString);
                outputString = hungarianString;
                break;
            //This case is to convert all Irish words
            case "ga":
            case "ga-IE":
                char c = wordSample.charAt(1);
                if (wordSample.startsWith("n") || wordSample.startsWith("t")) {
                    if (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U' || c == 'Á' || c == 'É' || c == 'Í' || c == 'Ó' || c == 'Ú') {
                        //Adding hyphen when condition satisfies
                        String IrishString1 = wordLowerCase.charAt(0) + "-" + wordLowerCase.substring(1);
                        System.out.println("String after converting to lower case: " + IrishString1);
                        outputString = IrishString1;
                    } else {
                        //Else for letters starting with "n" and "t", but not followed by capital vowels
                        System.out.println("String after converting to lower case: " + wordLowerCase);
                        outputString = wordLowerCase;
                    }
                } else {
                    //Else for letters not starting with "n" and "t"
                    System.out.println("String after converting to lower case: " + wordLowerCase);
                    outputString = wordLowerCase;
                }
                break;
            /*Default condition returns the word as is for any other language that do not have
            have any cases
             */
            default:
                System.out.println("String after converting to lower case: " + wordLowerCase);
                outputString = wordLowerCase;
                break;
        }
        return outputString;//returns the output lowercase word which is used for test code
    }
}

