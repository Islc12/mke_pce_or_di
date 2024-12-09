/*String inputData is read from input.
Use a for loop that iterates index i from inputData.length() - 1 down to 0 to output
the characters of inputData in reverse order, separated by dashes ('-').

Ex: If the input is apricot, then the output is:

t-o-c-i-r-p-a
*/

import java.util.Scanner;

public class reverse_a_string {
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      String inputData;
      int i;

      System.out.println("Enter a word to see it written backwards:");
      inputData = scnr.next();

      for (i = inputData.length() - 1; i >= 0; --i) {
         System.out.print(inputData.charAt(i));
         if (i > 0) {
            System.out.print("");
         }
      }

   }
}
