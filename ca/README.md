This program uses assertions to check the test cases provided.

Steps to compiling and running the code
----------------------------------------
1. Navigate to directory "/5030/ca/" on your command line interface
2. run "javac Main.java", this command compiles the source code and generates the byte code
3. run "java -ea Main", this executes the code

Note the "-ea" in the above command, this enables assertions since it is not enabled enabled by default in java.

OUTPUT
------
After invoking the "java -ea Main" command, a blank or empty output indicates success, all test cases passed.
On the other hand, a java.lang.AssertionError indicates failure, with an appropriate message.