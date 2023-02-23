import java.util.Locale;
// A class to convert the case of a character and a given string
public class CharacterCaseConverter {

    public static void main(String[] args) {

        // Convert the case of two characters
        char ch1 = 'T';
        char ch2 = 'P';
        ch1 = Character.toLowerCase(ch1);
        ch2 = Character.toLowerCase(ch2);

        // Display the result of each character's lowercase conversion
        String str1 = "The lowercase for the first character '" + ch1 + "' is given as: " + ch1;
        String str2 = "The lowercase for the second character '" + ch2 + "' is given as: " + ch2;
        System.out.println(str1);
        System.out.println(str2);

        // Convert the case of a given string using two different locales
        String myString = "YAŞAT Patel";
        Locale trlocale = new Locale("tr", "TR");
        Locale enLocale = new Locale("en", "US");
        String enResult = StringUtil.removeDiacritics(myString.toLowerCase(enLocale));
        String trResult = StringUtil.removeDiacritics(myString.toLowerCase(trlocale));

        // Display the result of the string's lowercase conversion for each locale
        System.out.println("en source: " + enResult);
        System.out.println("tr source: " + trResult);
    }
}
