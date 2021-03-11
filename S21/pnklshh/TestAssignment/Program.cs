using System;
using System.Collections.Generic;
using System.Globalization;

namespace TestAssignment
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            var runAllTests = false;    // To run all tests together, change the value to true

            if (runAllTests)
                Test.PerformTest();
            else
            {
                Console.WriteLine("Enter Word: ");
                string word = Console.ReadLine();
                Console.WriteLine("Enter Language: ");
                string language = Console.ReadLine();
                var lowerWord = ConvertToLowercase(word, language);
                Console.WriteLine("Lower word: " + lowerWord);
            }
        }

        public static string ConvertToLowercase(string word, string language)
        {
            var charList = new List<char>(word);
            var lowerCharList = new List<char>();
            var lowerWord = "";
            var culture = new CultureInfo(language);
            var vowelList = new List<char>() { 'A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú' };
            const string IRISH_CODE = "ga";
            const string Greek_CODE = "el";

            for (var i = 0; i < charList.Count; i++)
            {
                lowerCharList.Add(char.ToLower(charList[i], culture));
            }

            if (language.StartsWith(IRISH_CODE)                     // handle exception for Irish(if a word begins with a lowercase n or t immediately followed by an uppercase vowel, then a hyphen must be inserted as the second character when lowercasing)
                && (charList[0] == 'n' || charList[0] == 't')
                && (vowelList.Contains(charList[1])))
            {
                lowerCharList.Insert(1, '-');
            }
            else if(language.StartsWith(Greek_CODE) && charList[charList.Count - 1] == 'Σ')   // handle exception for Σ as last character in Greek
            {
                lowerCharList[charList.Count - 1] = 'ς';
            }

            foreach (var character in lowerCharList)
            {
                lowerWord += character.ToString();
            }

            return lowerWord;
        }
    }
}
