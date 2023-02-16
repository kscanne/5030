import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.*;
import java.util.Locale;

public class Conversion {
	public void conversionlogic() 
	{
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Please enter the word");
		String str = br.readLine();
		System.out.println("Please enter the language you would like to translate the word");
		String str_lang = br.readLine();
		PrintWriter out = new PrintWriter("oceans.txt"); 
		String output = str.toLowerCase(new Locale(str_lang));
		if(str_lang == " tr " || str_lang == "az")
		{
			if(str.contains("I")) 
			{
				str = str.replaceAll("I", " \0u131");
				output = str.toLowerCase(new Locale(str_lang));
			}
		}
		else if(str_lang.equals("ga-IE")|| str_lang.equals("ga") )
		{
	
			if((str.charAt(0) == 'n' || str.charAt(0) == 't')&& (str.charAt(1) == 'A' || str.charAt(1) == 'E' || str.charAt(1) == 'I' || str.charAt(1) == 'O' 
			|| str.charAt(1) == 'U'|| str.charAt(1) == 'Ó' || str.charAt(1) == 'Á' ||str.charAt(1) == 'É' || str.charAt(1) == 'Ú' ||str.charAt(1) == 'Í'))
			
			{
				
				output = output.substring(0,1) + "-" + output.substring(1);
			}
			
		}
		out.println(output);
		out.close();
	}

}
