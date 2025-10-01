class Solution {
    boolean solution(String s) {
        int left=0;//괄호의 수를 count 해주는 변수이다.

        for(int i=0;i<s.length();i++) {//문자열의 길이만큼 반복한다.
            char c = s.charAt(i);//문자열의 하나를 문자로 저장한다.
            if(c=='(') {
                left ++;
            } else {
                left --;
            }//왼쪽 괄호면 left를 +, 오른쪽 괄호면 left를 -한다.
            if(left<0) return false;//left가 -가 된다는 것은 오른쪽 괄호가 더 많아지는 경우를 의미하므로 false를 리턴한다.
        }
        return left==0;//left가 0이 아니더라도, left가 0이 아니면 올바른 괄호가 되지 않는다.
    }
}