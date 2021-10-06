package Review;

import java.util.*;

import java.util.Locale;

public class Main
{
	public static void main(String[] args) {
	    //English language
	            String strUpper, strLower;
        Scanner scan = new Scanner(System.in);
        
        System.out.println("Enter one word/name in Uppercase : ");
        strUpper = scan.nextLine();
        
        strLower = strUpper.toLowerCase();
        System.out.println("Equivalent Word/Name in Lowercase : " + strLower);
        
        

        // Turkish Language
        Locale.setDefault(new Locale("tr")); //setting Turkish as locale
        String str = "\u0131";
		   String toUpperCase, toLowerCase;
        Scanner s = new Scanner(System.in);
        
        System.out.println("Enter one word/name in Uppercase : ");
        toUpperCase = s.nextLine();
        
        toLowerCase = toUpperCase.toLowerCase();
        System.out.println("Equivalent Word/Name in Lowercase : " + toLowerCase);
        
        
        
        //Greek Language
        Locale.setDefault(new Locale("el")); //setting greek as locale
        String st = "\u03c2";
		   String toUpper, toLower;
        Scanner sca = new Scanner(System.in);
        
        System.out.println("Enter one word/name in Uppercase : ");
        toUpper = sca.nextLine();
        
        toLower = toUpper.toLowerCase();
        System.out.println("Equivalent Word/Name in Lowercase : " + toLower);



        //Irish Language
         Scanner sc = new Scanner(System.in);
        System.out.println("enter the word:");
         char[] sa = sc.next().toCharArray();
            String str1 = new String(sa);
        int n = str1.length();
        char ch = str1.charAt(0);
        char sech = str1.charAt(1);
        if(ch == 't' || ch == 'n')
        {
         if(sech == 'A' || sech == 'E' || sech == 'I' || sech == 'O' || sech == 'U'){
        
               char ssech = Character.toLowerCase(sech);
                 System.out.print(ch+ "-" +ssech);
                 for(int i=2; i<sa.length; i++){
                    System.out.print(sa[i]);
                            }
                }
            	}
	}
}