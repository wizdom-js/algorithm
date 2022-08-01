public int[] solution2(long n) {
  String s =""+n; //String에 n 추가
  int[] answer = new int[s.length()];//입력받은 숫자의 길이만큼
  int cnt=0;
  while(n>0) {
    answer[cnt]=(int)(n%10);//12345 -> 나머지 5 -> 4 -> 3 -> 2 ->1
    n/=10; // n=1234 -> 123 -> -> 12 -> 1
    cnt++;
  }
  return answer;
}
