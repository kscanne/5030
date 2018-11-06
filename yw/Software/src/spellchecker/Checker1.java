package spellchecker;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Checker1 {
	


	
  public  String check(String a) throws IOException {
	  
	  Read i = new Read();
	  List<String> s = new ArrayList();
	  
	  System.out.println("read method start working");

	  s = i.read();  // S is now a line of string that need to be get rid of
	  String b = a.toLowerCase();  //change everything to lowercase
	  String [] Arr = a.split("\\s+");  // split the original with space
	  String [] arr = b.split("\\s+");  // split the line with space
	  

      List<String> Ar= Arrays.asList(Arr);
	  System.out.println("core striping start working! ...");
	  List<Integer> suspect = new ArrayList();
	  
	  for(int e = 0;e<arr.length;e++) {
		  System.out.println(Arr[e]);
		  for(String sc : s) {
			  
			  if(arr[e].equals(sc)) {
				  
				  System.out.println(Ar + " " + e);
				  System.out.println(Ar.get(e));
                  suspect.add(e);
				//Ar.remove(Ar.get(e)) ;
				  System.out.println(Ar);

			  }
		  }
		  
	  }
	  System.out.println(suspect);
	  List<String> copyOfArr = new ArrayList();
	  for(int e=0;e<Arr.length;e++) {
		  if(suspect.indexOf(e)==-1) {
			  copyOfArr.add(Arr[e]);
		  }
	  }
	  String x = String.join(" ", copyOfArr);  
	  System.out.println("map all the remain element...");
	  
	  System.out.println(x + "!!!!!");
	  
	return x;
		

		
	}
  
  
  @SuppressWarnings("unchecked")
public List<String> read() throws IOException {
	  String target_dir = "C:\\Users\\wangyifei\\software\\5030\\data";
	  File dir = new File(target_dir);
	  File[] files = dir.listFiles();
	  List<String> myList = new ArrayList();
	  
	  for (File f : files) {
		  if(f.isFile()) {
			  BufferedReader inputStream = null;
			  
			  try {
				  inputStream = new BufferedReader(new FileReader(f));
				  String line;
				  
				  while ((line = inputStream.readLine())!=null) {
					  myList.add(line);
					  
				  }
			  }
			  finally {
				  if (inputStream != null) {
                      inputStream.close();
                  }
			  }
		  }
	  }
	System.out.println(myList);
	   
	return myList;
	
	  
  }
  
  
  
  
		
		
		//source sentences
		//String en = "the walking dead";
		//String ga = "Na daoine maithe";
		//String fr = "plus ça change, plus c'est la même chose";
		
//		String s = null;
//		String c = null;
//		while(true) {
//		System.out.println("Please input the language type:");
//		//input 
//		Scanner sc = new Scanner(System.in);
//		
//		s = sc.nextLine();
//		if("close".equals(s)) {
//		    System.out.println("System has been terminated!");
//		    sc.close();
//			return;
//		}
//		
//		if("en".equals(s)) {
//			System.out.println("Please input the santence:");
//			Scanner en = new Scanner(System.in);
//			c = en.nextLine();
//			c = c.replaceAll("the |The | the", "");
//			c = c.replaceAll(" the ", " ");
//		}else if("ga".equals(s)) {
//			System.out.println("Please input the santence:");
//			Scanner ga = new Scanner(System.in);
//			c = ga.nextLine();
//			c = c.replaceAll("Na | na|na ", "");
//			c = c.replaceAll(" na ", " ");
//
//		}else if("fr".equals(s)) {
//			System.out.println("Please input the santence:");
//			Scanner fr = new Scanner(System.in);
//			c = fr.nextLine();
//			c = c.replaceAll(" la|la |La ", "");
//			c = c.replaceAll(" la ", " ");
//
//		}else {
//			System.out.println("Input language typedoes not match!");
//			return;
//		}
//		//String e = "the ";
//		//String g = "Na ";
//		//String f = "la ";
//		
//		//String sub = s.replaceAll( "the |The | the |Na | na | na| la | la|la ","");
//        System.out.println("After checking: \n" + c);
//        //sc.close();
//		}
		
		
	

}
