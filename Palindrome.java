import java.util.Scanner;
class Palindrome {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        System.out.print("enter the name ;");
        String name = sc.nextLine();
        int length =name.length();
        int left = 0;
        int right = length -1;
        while(left<right){
            if(name.charAt(left)!=name.charAt(right)){
                System.out.println("not a pallindrome");
                break;
            }
            left++;
            right++;
        }
            if(left==right){
                 System.out.println("pallindrome");
        }
    
    }
}