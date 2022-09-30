import java.util.*;

class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char bracket = s.charAt(i);
            if (bracket == '(') {
                stack.push(bracket);
            } else {
                if (!stack.empty()) {
                    char beforeBracket = stack.peek();
                    if (beforeBracket == '(') {
                        stack.pop();
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
            }
        }
        return stack.empty() ? true : false;
    }
}