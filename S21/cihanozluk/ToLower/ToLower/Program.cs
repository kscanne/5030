using System;

namespace ToLower
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(new UpperToLower("HELLO", "en").ToGetLower());

            Console.WriteLine(new UpperToLower("WORLD", "en-US").ToGetLower());

            Console.WriteLine(new UpperToLower("cAmEl", "en-IE").ToGetLower());
            Console.WriteLine(new UpperToLower("---OK", "en-Latn").ToGetLower());

            Console.WriteLine(new UpperToLower("tAcht", "ga").ToGetLower());
            Console.WriteLine(new UpperToLower("tACHT", "ga").ToGetLower());
            Console.WriteLine(new UpperToLower("TACHT", "ga").ToGetLower());
            Console.WriteLine(new UpperToLower("nAthair", "ga").ToGetLower());
            Console.WriteLine(new UpperToLower("nATHAIR", "ga").ToGetLower());
            Console.WriteLine(new UpperToLower("NATHAIR", "ga").ToGetLower());
            Console.WriteLine(new UpperToLower("nÓg", "ga-IE").ToGetLower());
            Console.WriteLine(new UpperToLower("ASDnÓg", "ga-IE").ToGetLower());


            Console.WriteLine(new UpperToLower("KASIM", "tr").ToGetLower());
            Console.WriteLine(new UpperToLower("TATİL", "tr").ToGetLower());

            Console.WriteLine(new UpperToLower("KASIM", "en").ToGetLower());

            Console.WriteLine(new UpperToLower("ΠΌΛΗΣ", "el").ToGetLower());
            Console.WriteLine(new UpperToLower("ΠΌΛΗΣΠΌ", "el").ToGetLower());

            Console.WriteLine(new UpperToLower("官话", "zh-Hans").ToGetLower());
            Console.WriteLine(new UpperToLower("ภาษาไทย", "th").ToGetLower());
        }
    }
}
