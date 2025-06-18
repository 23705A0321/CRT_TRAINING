import java.util.Scanner;
class Main{
    public static void main(String[]args){
    Scanner sc = new Scanner(System.in);
    String name = sc.nextLine();
    int length= name.length();
    char []array = new char[length];
    char []reverse = new char[length];
    for(int i=0; i<name.length(); i++){
        array [i] = name.charAt(i);
    }
    int j=0;
    for(int i = length -1; i>=0 ; i--){
        reverse[j] = array[i];
        j++;
    }
    for(int i=0 ; i<length ; i++){
        System.out.print(reverse[i]);
    }
        
    }
}