import java.util.Locale;

public class LowerCasing {

    public static void main(String[] args)
    {

    }
    public String lowerCaseConversion(String languageType,String word)
    {
        String[] exceptedLanguages = {"zh" , "ja" , "th"};
        Locale locale = Locale.forLanguageTag(languageType);
        String language = locale.getLanguage();  
        for(String element : exceptedLanguages)
        {
            if(element.equals(language))
            {
                return word;
            }
        }
        String returningValue = word;
        if(language.equals("tr") || language.equals("az"))
        {
            returningValue = word.replace('I' ,'\u0131');
        }
        else if(language.equals("el"))
        {
            if (word.endsWith("Σ"))
            {
                returningValue = word.substring(0, word.length() - 1) + "\u03c2"; 
            }
            else
            {
                returningValue = word.replace("Σ", "σ");
            }
        }
        else if(language.equals("ga"))
        {
            if((word.charAt(0) == 'n' || word.charAt(0) == 't'))
            {
                char[] vowelArray = {'A','E','I','O'};
                boolean vowelsArePresent = false;
                for(int i = 0;i < vowelArray.length;i++)
                {
                    if(vowelArray[i] == word.charAt(1))
                    {
                        vowelsArePresent = true;
                        break;
                    }
                }
                if(vowelsArePresent)
                {
                    returningValue = word.charAt(0) + "-" + word.substring(1);
                }
            }
        }
        
       return returningValue.toLowerCase(locale);
    }    
}
