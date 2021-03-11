using System;
namespace ToLower
{
    public class Alphabet
    {
        public Alphabet(string language, string upper, string lower)
        {
            Language = language;
            Upper = upper;
            Lower = lower;
        }

        public string Language { get; set; }
        public string Upper { get; set; }
        public string Lower { get; set; }
    }
}
