import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.*;
import java.util.Locale;

public class Conversion {
	public static String trazConv(String str_lang, String str) {
		if (str.contains("I")) {
			str = str.replaceAll("I", "\u0131");
			return str.toLowerCase(new Locale(str_lang));
		} else {
			return str.toLowerCase(new Locale(str_lang));
		}
	}

	public static String gaConv(String str_lang, String str) {

		if (("nt".indexOf(str.charAt(0)) != -1)
				&& ("AEIOUÁÉÚÍÓ".indexOf(str.charAt(1)) != -1))

		{
			String k;
			k = str.toLowerCase(new Locale(str_lang));
			String m = (k.substring(0, 1) + "-" + k.substring(1));
			return m;
		} else {
			return str.toLowerCase(new Locale(str_lang));
		}

	}

	public static String allConv(String str_lang, String str) {
		return (str.toLowerCase(new Locale(str_lang)));
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Please enter the word");
		String str = br.readLine();
		System.out.println("Please enter the language you would like to translate the word");
		String str_lang = br.readLine();
		PrintWriter out = new PrintWriter("output.txt");
		String output = str.toLowerCase(new Locale(str_lang));
		if (str_lang.equals("tr") || str_lang.equals("az")) {
			output = trazConv(str_lang, str);
		} else if (str_lang.contains("ga")) {
			output = gaConv(str_lang, str);
		} else {
			output = allConv(str_lang, str);
		}
		out.println(output);
		out.close();
	}

}
