def solution(record):
    log = {}
    ment = []
    answer = []

    enter_chat = "님이 들어왔습니다."
    leave_chat = "님이 나갔습니다."

    for chat in record :
        if chat.count(" ") == 2 :
            state, user, name = chat.split(" ")
        else :
            state, user = chat.split(" ")

        if state == "Enter" :
            log[user] = name
            ment.append([user, enter_chat])
        elif state == "Leave" :
            ment.append([user, leave_chat])
        elif state == "Change" :
            log[user] = name

    for i in ment :
        answer.append(log[i[0]]+i[1])

    return answer
