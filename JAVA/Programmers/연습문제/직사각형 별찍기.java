import java.util.Scanner;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        String star = "*".repeat(n);
        for (int i = 0; i < m; i++) {
            System.out.println(star);
        }
    }
}