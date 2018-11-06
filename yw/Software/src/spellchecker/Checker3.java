package spellchecker;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Checker3 {

	public String checker3(String arr, String lan) throws IOException {
		Read1 r = new Read1();
		String[] sentence = arr.split("\\s+"); 
		List<String> stopwords = r.read1(lan);  // receive suspects
		List<String> arrList = new ArrayList();
//		System.out.println(suspects);
	
		for(int i = 0; i < sentence.length;i++) {
			String word = sentence[i].toLowerCase();
			
			if(stopwords.indexOf(word) ==-1 && word.length() > 0) {
				arrList.add(sentence[i]);
			}
			
			
		}
		
		arr = String.join(" ", arrList);
		
		return arr;
		// TODO Auto-generated constructor stub
	}

	

}
