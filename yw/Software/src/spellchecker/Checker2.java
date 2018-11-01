package spellchecker;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Checker2 {

	public String check(String arr) throws IOException {
		Read r = new Read();
		String[] sentence = arr.split("\\s+"); 
		List<String> suspects = r.read();  // receive suspects
		List<String> arrList = new ArrayList();
//		System.out.println(suspects);
	
		for(int i = 0; i < sentence.length;i++) {
			String word = sentence[i].toLowerCase();
			
			if(suspects.indexOf(word) ==-1 && word.length() > 0) {
				arrList.add(sentence[i]);
			}
			
			
		}
		
		arr = String.join(" ", arrList);
		
		return arr;
		// TODO Auto-generated constructor stub
	}

}
