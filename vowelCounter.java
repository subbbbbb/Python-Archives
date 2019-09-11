import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter your word and I'll tell you how many vowels there are::");
    String word = sc.nextLine();
    int vowCount = 0;
    for (int i = 0; i < word.length(); i++) {
      if (word.substring(i, i + 1).equals("a") || word.substring(i, i + 1).equals("e")
          || word.substring(i, i + 1).equals("i") || word.substring(i, i + 1).equals("o")
          || word.substring(i, i + 1).equals("u")) {
        vowCount++;
      }
    }
    if(vowCount > 0)
      System.out.println("Your word has a total of " + vowCount + " vowels.");
    else System.out.println("Your word has no vowels in it.");
  }
}
