import java.text.Normalizer;
public class StringUtil {

  // A static method to remove diacritics from a given string
  public static String removeDiacritics(String s) {
      // Normalize the string using the NFD form
      String s2 = Normalizer.normalize(s, Normalizer.Form.NFD);
      // Replace all combining diacritical marks with an empty string
      return s2.replaceAll("(?s)\\p{InCombiningDiacriticalMarks}", "");
  }
}
