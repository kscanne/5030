package main;

import static org. junit.Assert.*;  
  
import org.junit.Test;

import com.firstspringproject.Controllers.ConvertToLowerCase;  
  
public class TestCasesJunit {
    
    ConvertToLowerCase obj = new ConvertToLowerCase();
    String langWithNoLowerCase[] = {"zh", "ja", "th"};

    @Test  
    public void testcase1() {  
       assertEquals("hello", obj.wordToLowerCase("HELLO","en",langWithNoLowerCase));   
    }  

    @Test  
    public void testcase2() {  
       assertEquals("world", obj.wordToLowerCase("WORLD","en-US",langWithNoLowerCase));   
    }  

    @Test  
    public void testcase3() {  
       assertEquals("camel", obj.wordToLowerCase("cAmEl","en-IE",langWithNoLowerCase));   
    }  

    @Test  
    public void testcase4() {  
       assertEquals("---ok", obj.wordToLowerCase("---OK","en-Latn",langWithNoLowerCase));   
    }  

    @Test  
    public void testcase5() {  
       assertEquals("t-acht", obj.wordToLowerCase("tAcht","ga",langWithNoLowerCase));   
    }  

    @Test  
    public void testcase6() {  
       assertEquals("t-acht", obj.wordToLowerCase("tACHT","ga",langWithNoLowerCase));   
    }  

    @Test  
    public void testcase7() {  
       assertEquals("tacht", obj.wordToLowerCase("TACHT","ga",langWithNoLowerCase));   
    }  

    @Test  
    public void testcase8() {  
       assertEquals("n-athair", obj.wordToLowerCase("nAthair","ga",langWithNoLowerCase));   
    }  

    @Test  
    public void testcase9() {  
       assertEquals("n-athair", obj.wordToLowerCase("nATHAIR","ga",langWithNoLowerCase));   
    }  

    @Test  
    public void testcase10() {  
       assertEquals("nathair", obj.wordToLowerCase("NATHAIR","ga",langWithNoLowerCase));   
    }  

    @Test  
    public void testcase11() {  
       assertEquals("t-othair", obj.wordToLowerCase("tOthair","ga",langWithNoLowerCase));   
    }  

    @Test  
    public void testcase12() {  
       assertEquals("t-ethair", obj.wordToLowerCase("tETHAIR","ga",langWithNoLowerCase));   
    }  

    @Test  
    public void testcase13() {  
       assertEquals("t-ithair", obj.wordToLowerCase("tITHAIR","ga",langWithNoLowerCase));   
    }  

    @Test  
    public void testcase14() {  
       assertEquals("n-óg", obj.wordToLowerCase("nÓg","ga-IE",langWithNoLowerCase));   
    }  

    @Test  
    public void testcase15() {  
       assertEquals("nõg", obj.wordToLowerCase("nÕg","ga-IE",langWithNoLowerCase));   
    }  

    @Test  
    public void testcase16() {  
       assertEquals("对不起", obj.wordToLowerCase("对不起","zh",langWithNoLowerCase));   
    }  

    @Test  
    public void testcase17() {  
       assertEquals("ごめんなさい", obj.wordToLowerCase("ごめんなさい","ja",langWithNoLowerCase));   
    }  

    @Test  
    public void testcase18() {  
       assertEquals("kasım", obj.wordToLowerCase("KASIM","az",langWithNoLowerCase));   
    }  

    @Test  
    public void testcase19() {  
       assertEquals("kasim", obj.wordToLowerCase("KASIM","en",langWithNoLowerCase));   
    } 
    
    @Test  
    public void testcase20() {  
       assertEquals("πόλης", obj.wordToLowerCase("ΠΌΛΗΣ","el",langWithNoLowerCase));   
    }  

    @Test  
    public void testcase21() {  
       assertEquals("官话", obj.wordToLowerCase("官话","zh-Hans",langWithNoLowerCase));   
    }  

    @Test  
    public void testcase22() {  
       assertEquals("ภาษาไทย", obj.wordToLowerCase("ภาษาไทย","th",langWithNoLowerCase));   
    }  

    @Test  
    public void testcase23() {  
       assertEquals("πόλης", obj.wordToLowerCase("ΠΌΛΗΣ","el-GR",langWithNoLowerCase));   
    } 
    
    @Test  
    public void testcase24() {  
       assertEquals("πόλησπόλης", obj.wordToLowerCase("ΠΌΛΗΣΠΌΛΗΣ","el-GR",langWithNoLowerCase));   
    } 
}
