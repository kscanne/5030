package diana;

import java.util.Locale;
import java.util.Scanner;

/**
 * The WordToLowerCase program implements an application that
 * gets a word and its language and converts all the letters
 * to the lowercase.
 *
 * @author  Diana Stelmakh
 */
public class WordToLowerCase {

    /**
     * This is the main method which ask user to input the word
     * and the language, and uses changeWordToLowerCase()
     * to convert it to lowercase.
     *
     * @param args Unused.
    */
    public static void main(String[] args) {
        System.out.println("Enter the word to convert to lowercase:");
        Scanner in = new Scanner(System.in);
        String wordForLowerCase = in.nextLine();

        System.out.println("Enter the language (BCP-47 specification:");
        String language = in.nextLine();

        changeWordToLowerCase(wordForLowerCase, language);
    }

    /**
     * This is the method that converts the word to lowercase
     * and looks for the exception in certain languages
     * @param oldWord the String for the input word.
     * @param language the String for the language of the word.
     * @return word changed to lowercase
    */
    public static String changeWordToLowerCase(String oldWord, String language) {
        String wordToProcess = oldWord;

        Locale.setDefault(new Locale(language));

        // Irish (ga) exceptions
        if ("ga".equals(language) || "ga-IE".equals(language)) {
            String[] lettersExceptions = {"A", "E", "I", "O", "U", "Á", "É", "Í", "Ó", "Ú"};
            for (int i = 0; i < lettersExceptions.length - 1; i++) {
                if (wordToProcess.substring(0, 2).equals("n" + lettersExceptions[i])
                        || wordToProcess.substring(0, 2).equals("t" + lettersExceptions[i])) {
                    wordToProcess = wordToProcess.replaceFirst(lettersExceptions[i],
                            "-" + lettersExceptions[i]);
                }
            }
        }

        String lowerCasedWord = wordToProcess.toLowerCase();
        System.out.println(lowerCasedWord);
        return lowerCasedWord;
    }
}
