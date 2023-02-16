new Locale(language)
new Locale(language, country)
new Locale(language, country, variant)

class JavaCharactertoLowerCaseExample1 {  
  public static void main(String[] args) {  
		
		String s2 = Normalizer.normalize(s, Normalizer.Form.NFD);
    		return s2.replaceAll("(?s)\\p{InCombiningDiacriticalMarks}", "");

     char ch1, ch2, ch3, ch4;    
      ch1 = 'TANVI';  
      ch2 = 'PATEL';  
        
      ch3 = Character.toLowerCase(ch1);  
      ch4 = Character.toLowerCase(ch2);  
      String str1 = "The lowercase for the first character '" + ch1 + "' is given as: " + ch3;  
      String str2 = "The lowercase for the second character '" + ch2 + "' is given as: " + ch4;  
  
      System.out.println( str1 );  
      System.out.println( str2 );  
      }  
}  

String myString="YAŞAT Patel";
Locale trlocale= new Locale("tr-TR");
Locale enLocale = new Locale("en_US");

Log.v("mainlist", "en source: " +myString.toLowerCase(enLocale));
Log.v("mainlist", "tr source: " +myString.toLowerCase(trlocale));
