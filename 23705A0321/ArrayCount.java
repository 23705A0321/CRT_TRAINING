import java.util.Scanner;
class Main{
    public static void main(String[]args){
    Scanner sc = new Scanner(System.in);
    String name = sc.nextLine();
    char[] array = name.toCharArray();
    int count = 0;
    for(int left = 0 ; left<name.length(); left++){
        count = 1;
    for(int right = left +1; right < name.length() ; right++){
        if(array[left] == '_'){
        continue;
    }
    else if(array[left] == array[right]){
        count++;
        array[right] = '_';
        }
    }
    if(array[left] != '_'){
        System.out.println(array[left] + " = " + count);
        }
    }
    }