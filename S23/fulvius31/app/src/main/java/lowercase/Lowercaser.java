package lowercase;

import java.text.Normalizer;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Lowercaser {

    private final String upperCase;
    private final String lang;
    private char[] strChar;

    public Lowercaser(String upperCase, String lang) {
        this.upperCase = upperCase;
        this.lang = lang.split("-")[0];
    }

    private String lowerTrAz() {
        for (int i = 0; i < strChar.length; i++) {
            if (strChar[i] == 'I')
                strChar[i] = 'ı';
            else
                strChar[i] = Character.toLowerCase(strChar[i]);
        }
        return new String(strChar);
    }

    private String lowerGa() {
        Set<String> irishVowels = new HashSet<>
                (Arrays.asList("A", "E", "I", "O", "U", "Á", "É", "Í", "Ó", "Ú"));
        String normalizedUpper = Normalizer.normalize(upperCase,
                Normalizer.Form.NFC);

        StringBuilder sb = new StringBuilder();
        boolean isSpecialCase = false;
        for (int i = 0; i < normalizedUpper.length(); i++) {
            String ch = normalizedUpper.substring(i, i + 1);
            if (i == 0 && (ch.contains("n") || ch.contains("t"))) {
                isSpecialCase = true;
            }
            if (i == 1 && irishVowels.contains(ch) && isSpecialCase) {
                sb.append("-");
            }
            sb.append(ch.toLowerCase());
        }
        return sb.toString();
    }

    private String lowerEl() {
        int strCharLength = strChar.length;
        if (strChar[strCharLength - 1] == 'Σ') {
            strChar[strCharLength - 1] = 'ς';
            strCharLength--;
        }
        for (int i = 0; i < strCharLength; i++) {
            strChar[i] = Character.toLowerCase(strChar[i]);
        }
        return new String(strChar);
    }

    public String getLowerCase() {
        if (isUnchangedLang())
            return upperCase;
        if (!isExceptionLang())
            return upperCase.toLowerCase();
        strChar = upperCase.toCharArray();
        if (lang.equals(LanguagesToExamine.AZERBAIJANI.getAcronym()) ||
                lang.equals(LanguagesToExamine.TURKISH.getAcronym())) {
            return lowerTrAz();
        }
        if (lang.equals(LanguagesToExamine.IRISH.getAcronym())) {
            return lowerGa();
        }
        if (lang.equals(LanguagesToExamine.GREEK.getAcronym())) {
            return lowerEl();
        }

        return upperCase;
    }

    private boolean isUnchangedLang() {
        return lang.equals(LanguagesToExamine.CHINESE.getAcronym()) ||
                lang.equals(LanguagesToExamine.JAPANESE.getAcronym()) ||
                lang.equals(LanguagesToExamine.THAI.getAcronym());
    }

    private boolean isExceptionLang() {
        return lang.equals(LanguagesToExamine.TURKISH.getAcronym()) ||
                lang.equals(LanguagesToExamine.AZERBAIJANI.getAcronym()) ||
                lang.equals(LanguagesToExamine.IRISH.getAcronym()) ||
                lang.equals(LanguagesToExamine.GREEK.getAcronym());
    }

    enum LanguagesToExamine {
        TURKISH("tr"),
        AZERBAIJANI("az"),
        IRISH("ga"),
        GREEK("el"),
        CHINESE("zh"),
        JAPANESE("ja"),
        THAI("th");

        private final String acronym;

        LanguagesToExamine(String acronym) {
            this.acronym = acronym;
        }

        public String getAcronym() {
            return acronym;
        }
    }
}

