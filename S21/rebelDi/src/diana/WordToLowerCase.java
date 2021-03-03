package diana;

import java.util.*;

public class WordToLowerCase {

    public static void main(String[] args) {
        System.out.println("Enter the word to convert to lowercase:");
        Scanner in = new Scanner(System.in);
        String wordForLowerCase = in.nextLine();

        System.out.println("Enter the language (in form of BCP-47 specification:");
        String language = in.nextLine();

        changeWordToLowerCase(wordForLowerCase, language);
    }

    public static String changeWordToLowerCase (String word, String language) {
        Locale.setDefault(new Locale(language));

        // Irish (ga) exceptions
        if (language.equals("ga") || language.equals("ga-IE")) {
            String[] lettersExceptions = {"A", "E", "I", "O", "U", "Á", "É", "Í", "Ó", "Ú"};
            for (int i = 0; i < lettersExceptions.length - 1; i++) {
                if (word.substring(0, 2).equals("n" + lettersExceptions[i]) || word.substring(0, 2).equals("t" + lettersExceptions[i])) {
                    word = word.replaceFirst(lettersExceptions[i], "-" + lettersExceptions[i]);
                }
            }
        }

        String lowerCasedWord = word.toLowerCase();
        System.out.println(lowerCasedWord);
        return lowerCasedWord;
    }
}
