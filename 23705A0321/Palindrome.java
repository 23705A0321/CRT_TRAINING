import java.util.Scanner;
class Main{
    public static void main(String[]args){
    Scanner sc = new Scanner(System.in);
    String name = sc.nextLine();
    int left = 0;
    int right = name.length() -1;
    while(left < right){
        if (name.charAt(left) == name.charAt(right)) {
            System.out.println("not palindrome");
            break;
        }
        else{
            System.out.println("palindrome");
        }
        left++;
        right++;
    }
    if(name.charAt(right) == name.charAt(left)){
        
    System.out.println("palindrome");
    }