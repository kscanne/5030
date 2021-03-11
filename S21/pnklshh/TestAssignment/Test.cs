using System;
using System.Collections.Generic;
using System.Text;
using System.IO;

namespace TestAssignment
{
    class Test
    {
        public static void PerformTest()
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;

            Console.WriteLine("Enter the path of tsv file: ");
            var path = Console.ReadLine();
            var testInput = File.ReadAllLines(path);
            Console.WriteLine("\n Output for each test case: \n");

            foreach (var input in testInput)
            {
                var word = input.Split('\t')[0];
                var language = input.Split('\t')[1];

                var lowerWord = Program.ConvertToLowercase(word, language);
                Console.WriteLine(word + '\t' + language + '\t' + lowerWord);
            }
        }
    }
}
