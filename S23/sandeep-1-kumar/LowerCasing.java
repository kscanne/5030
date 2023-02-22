import java.util.Locale;
public class LowerCasing {

    public int upperCaseIrishA = 193;
    public int upperCaseIrishE = 201;
    public int upperCaseIrishI = 205;
    public int upperCaseIrishO = 211;
    public int upperCaseIrishU = 218; 

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
        if(language.startsWith("tr") || language.startsWith("az"))
        {   //->'/u0131' is a Unicode representation of the lowercase dotless I.
             returningValue =word.replaceAll("[iI]", "\u0131");
        }
        else if(language.startsWith("el"))
        {
            if (word.endsWith("Σ"))
            {   //->'/u03c2' is a Unicode representation of the lowercase Greek letter 'ς'
                returningValue = word.substring(0, word.length() - 1) + "\u03c2"; 
            }
            else
            {
                returningValue = word.replace("Σ", "σ");
            }
        }
        else if(language.startsWith("ga")  )
        {   
            if((word.charAt(0) == 'n' || word.charAt(0) == 't'))
            {
                char[] vowelArray = {'A','E','I','O','U'};
                int[] irishVowelsArray={upperCaseIrishA,upperCaseIrishE,upperCaseIrishI,upperCaseIrishO,upperCaseIrishU};
                boolean vowelsArePresent = false;
                for(int i = 0;i < vowelArray.length;i++)
                {
                    if(vowelArray[i] == word.charAt(1) || irishVowelsArray[i] == word.charAt(1) )
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
