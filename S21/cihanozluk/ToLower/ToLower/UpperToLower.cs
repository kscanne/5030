using System;
using System.Collections.Generic;
using System.Text;
namespace ToLower
{
    public class UpperToLower
    {

        public UpperToLower(string word, string language)
        {
            if (string.IsNullOrEmpty(language))
            {
                throw new ArgumentException($"'{nameof(language)}' cannot be null or empty.", nameof(language));
            }
            Word = word ?? throw new ArgumentNullException(nameof(word));
            Language = language;

        }


        public string Word { get; }

        public string Language { get; }


        private string GetToLower() => Word.ToLower(new System.Globalization.CultureInfo(Language));

        public string ToGetLower()
        {
            List<Alphabet> alphabets = new List<Alphabet>();
            alphabets.Add(new Alphabet("tr", "ABCÇDEFHĞHIİJKLMNOÖPQRSŞTUÜVWXYZ", "abcçdefgğhıijklmnoöpqrsştuüvwxyz"));
            alphabets.Add(new Alphabet("el", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ", "αβγδϵζηθικλμνξοπρστυϕχψω"));
            alphabets.Add(new Alphabet("ga", "ABCDEFGHILMNOPRSTUÁÉÍÓÚ", "abcdefghilmnoprstuáéíóú"));
            alphabets.Add(new Alphabet("ga-IE", "ABCDEFGHILMNOPRSTUÁÉÍÓÚ", "abcdefghilmnoprstuáéíóú"));

            if (Language != "tr" && Language != "el" && Language != "ga" && Language != "ga-IE")
                return GetToLower();
            else
            {
                var lowerWord = new StringBuilder();
                var str = alphabets.Find(r => r.Language == Language);



                foreach (char item in Word)
                {

                    lowerWord.Append(GetToLowerChar(item, str));
                }

                if (Language == "el" && Word.Substring(Word.Length - 1, 1) == "Σ")
                {
                    lowerWord[Word.Length - 1] = 'ς';
                }
                if ((Language == "ga" || Language == "ga-IE") && (Word.Substring(0, 1) == "n" || (Word.Substring(0, 1) == "t" && str.Upper.IndexOf(Word.Substring(1, 1)) >= 0)))
                {
                    lowerWord.Insert(1, "-");
                }
                return lowerWord.ToString();
            }
        }
        private char GetToLowerChar(char charOfWord, Alphabet alphabets)
        {

            int positonOfChar = alphabets.Upper.IndexOf(charOfWord);

            char getLowerChar;
            if (positonOfChar >= 0)
                getLowerChar = char.Parse(s: alphabets.Lower.Substring(positonOfChar, 1));
            else
                getLowerChar = charOfWord;

            return getLowerChar;
        }
    }
}
