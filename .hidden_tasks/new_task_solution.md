Here is a simplified code to perform the required task:

```java
public class Solution {
    public static void main(String[] args){
        System.out.println(addLargeNumbers("333", "777")); 
        System.out.println(addLargeNumbers("12345678901234567890", "98765432109876543210")); 
        System.out.println(addLargeNumbers("999999999999999", "1")); 
        System.out.println(addLargeNumbers("0", "0")); 
    }

    public static String addLargeNumbers(String num1, String num2) {
        StringBuilder result = new StringBuilder();

        int i = num1.length() - 1;
        int j = num2.length() - 1;

        int carry = 0;

        while (i >= 0 || j >= 0) {
            int sum = carry;

            if (i >= 0) {
                sum += num1.charAt(i) - '0';
                i--;
            }

            if (j >= 0) {
                sum += num2.charAt(j) - '0';
                j--;
            }

            result.append(sum % 10);
            carry = sum / 10;
        }

        if (carry != 0) {
            result.append(carry);
        }

        return result.reverse().toString();
    }
}
``` 

In this solution, we just simulated the manual addition method. Start adding numbers from the least significant digit and carry to the next position when sum exceeds 9.