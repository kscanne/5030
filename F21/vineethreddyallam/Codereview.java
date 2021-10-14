package Review;
import java.util.Locale;

public class Codereview {

	public static void main(String[] args) {
		
		//English
        String a, b;
        a = "HELLO WORLD";
        b = a.toLowerCase();
        System.out.println("English Word in Lowercase : " + b);



        // Turkish 
        Locale.setDefault(new Locale("tr")); 
        String str = "\u0131";
        String TU, TL;
        TU = "KASIM";
        TL = TU.toLowerCase();
        System.out.println("Turkish Word in Lowercase : " + TL);



        //Greek
        Locale.setDefault(new Locale("el")); 
        String st = "\u03c2";
        String GU, GL;
        GU = "ΠΌΛΗΣ";
        GL = GU.toLowerCase();
        System.out.println("Greek Word in Lowercase : " + GL);



        //Irish  
        String TUC = "nAthair";
        char[] TU1 = TUC.toCharArray();
        String s = new String(TU1);		
        char i = s.charAt(0);
        char k = s.charAt(1);
        if(i == 't' || i == 'n')
        {
        	if(k == 'A' || k == 'E' || k == 'I' || k == 'O' || k == 'U')
        	{

        		char m = Character.toLowerCase(k);
        		System.out.print("Irish Word in Lowercase : " + i+ "-" +m);
        		
        		for(int j=2; j<TU1.length; j++) {
        			System.out.print(TU1[j]);}
                    
        	}
        	
    	}
        else {
        	 String TU2 = TUC.toLowerCase();
             System.out.println("Turkish Word in Lowercase : " + TU2);
        	}
	}

}
