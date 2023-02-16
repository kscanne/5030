import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a word: ");
        String word = scanner.nextLine();
        System.out.print("Enter the language code (e.g. en-US, tr-TR, el-GR): ");
        String languageCode = scanner.nextLine();
        String lowerCaseWord = LowerCase.toLowerCase(word, languageCode);
        System.out.println("Lowercase word: " + lowerCaseWord);
        scanner.close();
    }

    public static class LowerCase {
        public static String toLowerCase(String word, String language) {
            Locale locale = language != null && !language.isEmpty() ? Locale.forLanguageTag(language) : Locale.getDefault();

            String lowerCaseWord;
            String languageTag = locale.toLanguageTag();

            if (languageTag.startsWith("tr") || languageTag.startsWith("az")) lowerCaseWord = word.replace("I", "ı");
            else if (languageTag.startsWith("ga")) {
                lowerCaseWord = lowerCaseIrish(word);
            } else if (languageTag.startsWith("el")) {
                lowerCaseWord = lowerCaseGreek(word);
            } else if (languageTag.startsWith("zh") || languageTag.startsWith("ja") || languageTag.startsWith("th")) {
                return word;
            } else {
                lowerCaseWord = word.toLowerCase(locale);
            }

            return lowerCaseWord;
        }

        public static String lowerCaseIrish(String word) {
            return word;
        }

        public static String lowerCaseGreek(String word) {
            return word;
        }
    }
}