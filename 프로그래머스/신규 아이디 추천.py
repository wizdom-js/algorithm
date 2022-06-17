import re
def solution(new_id):
    # 1. 소문자로 변환
    new_id = new_id.lower()
    
    # 2. 특수문자 제거
    new_id = re.sub('[^a-z0-9\.\_\-]','',new_id) 
    
    # 3. 마침표가 연속인 부분 치환
    new_id = re.sub('\.\.+', '.', new_id)
    
    # 4. 마침표가 처음이나 끝에 위치하면 제거
    new_id = re.sub('^\.|\.$', '', new_id)
    
    # 5. 빈 문자열이면 "a" 대입
    if new_id == "" :
        new_id = "a"
    
    # 6. 15자 이하로 맞추기
    if len(new_id) > 15 :
        new_id = re.sub('\.$', '', new_id[0:15])
    
    # 7. 2자 이하이면 마지막 문자 반복
    for i in range(3) :
        if len(new_id) < 3 :
             new_id = new_id + new_id[-1] 
            
    answer = new_id
    
    return answer