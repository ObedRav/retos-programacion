
public class index {

    public static void main(String[] args) {
        fizzbuzz(100);
    }

    public static void fizzbuzz(int num) {
        for (int i = 1; i <= num; i++) {
            String result = "";

            if (i % 3 == 0) {
                result = result.concat("fizz");
            }

            if (i % 5 == 0) {
                result = result.concat("buzz");
            }

            if (result.length() > 0) {
                System.out.println(result);
            } else {
                System.out.println(i);
            }
        }
    }
}
