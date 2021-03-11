//Test code to test different test cases
package com.company;

import org.junit.Test;//Package to perform unit testing

import static org.junit.Assert.assertEquals;//Asserts to see if 2 strings are equal

public class ConvertToLowerCaseTest {
    @Test
    public void testLowerCase(){
        ConvertToLowerCase convertToLowerCase = new ConvertToLowerCase();
        assertEquals("hello", convertToLowerCase.convert("HELLO", "en"));
        assertEquals("world",convertToLowerCase.convert("WORLD", "en-US"));
        assertEquals("camel",convertToLowerCase.convert("cAmEl", "en-IE"));
        assertEquals("---ok",convertToLowerCase.convert("---OK", "en-Latn"));
        assertEquals("t-acht",convertToLowerCase.convert("tAcht", "ga"));
        assertEquals("t-acht",convertToLowerCase.convert("tACHT", "ga"));
        assertEquals("tacht",convertToLowerCase.convert("TACHT", "ga"));
        assertEquals("n-athair",convertToLowerCase.convert("nAthair", "ga"));
        assertEquals("n-athair",convertToLowerCase.convert("nATHAIR", "ga"));
        assertEquals("nathair",convertToLowerCase.convert("NATHAIR", "ga"));
        assertEquals("n-óg",convertToLowerCase.convert("nÓg", "ga-IE"));
        assertEquals("kasım",convertToLowerCase.convert("KASIM", "tr"));
        assertEquals("kasim",convertToLowerCase.convert("KASIM", "en"));
        assertEquals("πόλης",convertToLowerCase.convert("ΠΌΛΗΣ", "el"));
        assertEquals("官话",convertToLowerCase.convert("官话", "zh-Hans"));
        assertEquals("ภาษาไทย",convertToLowerCase.convert("ภาษาไทย", "th"));
        assertEquals("привет",convertToLowerCase.convert("ПРИВЕТ", "ru"));
        assertEquals("világ",convertToLowerCase.convert("VILÁG","hu"));
        assertEquals("विश्व",convertToLowerCase.convert("विश्व","hi"));
        assertEquals("σιοντι",convertToLowerCase.convert("ΣΙΟΝΤΙ", "el"));
    }
}
