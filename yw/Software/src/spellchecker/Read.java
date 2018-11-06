package spellchecker;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Read {

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
		
		   
		return myList;
		
		  
	  }
}
