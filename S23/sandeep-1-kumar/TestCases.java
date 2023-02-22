import static org.junit.Assert.*;
import org.junit.Test;

public class TestCases {
//Testing and asserting different english words
    @Test
    public void testEnglish() {
        LowerCasing lc = new LowerCasing();
        assertEquals("hello", lc.lowerCaseConversion("en", "Hello"));
        assertEquals("advaccdfcxl", lc.lowerCaseConversion("en-US", "ADvaccdFCXl"));
        assertEquals("good morning", lc.lowerCaseConversion("en-IE", "gOOd Morning"));
        assertEquals("multipleassertions", lc.lowerCaseConversion("en", "muLtiPleAssertioNs"));
        assertEquals("---ok", lc.lowerCaseConversion("en-Latn", "---OK"));
        
    }
//Testing and asserting different turkish words
    @Test
    public void testTurkish() {
        LowerCasing lc = new LowerCasing();
        assertEquals("ışık", lc.lowerCaseConversion("tr", "IŞIK"));
        assertEquals("ığdır", lc.lowerCaseConversion("tr", "IĞDIR"));
        assertEquals("kasım", lc.lowerCaseConversion("tr", "KASIM"));
        assertEquals("istanbul", lc.lowerCaseConversion("tr", "İSTANBUL"));
    }
//Testing and asserting different turkish words
    @Test
    public void testAzerbaijanLanguage() {
    LowerCasing lc = new LowerCasing();
    assertEquals("salam", lc.lowerCaseConversion("az", "SALAM"));
    assertEquals("növbəti", lc.lowerCaseConversion("az", "NÖVBƏTİ"));
    assertEquals("baku", lc.lowerCaseConversion("az", "BAKU"));
    assertEquals("sığorta", lc.lowerCaseConversion("az", "SIĞORTA"));
    }
//Testing and asserting different Greek words
    @Test
    public void testGreek() {
        LowerCasing lc = new LowerCasing();
        assertEquals("ελληνικ", lc.lowerCaseConversion("el", "ΕΛΛΗΝΙΚ"));
        assertEquals("πόλης", lc.lowerCaseConversion("el", "ΠΌΛΗΣ"));
        assertEquals("συνεντευξη", lc.lowerCaseConversion("el", "ΣΥΝΕΝΤΕΥΞΗ"));
        assertEquals("της ελληνικς", lc.lowerCaseConversion("el", "ΤΗΣ ΕΛΛΗΝΙΚΣ"));
    }
//Testing and asserting different Irish words
    @Test
    public void testIrish() {
        LowerCasing lc = new LowerCasing();
        assertEquals("n-athair", lc.lowerCaseConversion("ga", "nATHAIR"));
        assertEquals("tsiopa", lc.lowerCaseConversion("ga-IE", "tsiopa"));
        assertEquals("n-éan", lc.lowerCaseConversion("ga", "nÉan"));
        assertEquals("lámh", lc.lowerCaseConversion("ga", "LÁMH"));
        assertEquals("n-óg", lc.lowerCaseConversion("ga-IE", "nÓg"));
        assertEquals("nõg", lc.lowerCaseConversion("ga", "nÕg"));
    }
//Testing and asserting other languages 
    @Test
    public void testJapanese() {
        LowerCasing lc = new LowerCasing();
        assertEquals("こんにちは", lc.lowerCaseConversion("ja", "こんにちは"));
    }
    @Test
    public void testLowerCaseConversionForThai() {
        LowerCasing lc = new LowerCasing();
        assertEquals("กรุงเทพมหานคร", lc.lowerCaseConversion("th", "กรุงเทพมหานคร"));
    }
    @Test
    public void testUnsupportedLanguage() {
        LowerCasing lc = new LowerCasing();
        assertEquals("hello", lc.lowerCaseConversion("zz", "HELLO"));
    }
}
